import logging
import os
import json
import pdfplumber
from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
import docx2txt
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain import PromptTemplate
import openai
import os

GPT_MODEL="gpt-3.5-turbo-0613"
openai.api_key=os.getenv("OPENAI_API_KEY")

# Configure logging
log_dir = os.getenv('LOG_DIRECTORY', './')
log_file_path = os.path.join(str(log_dir), 'app.log')

logging.basicConfig(
    filename=log_file_path,
    filemode='a',
    format='[%(asctime)s] [%(levelname)s] [%(filename)s] [%(lineno)s:%(funcName)5s()] %(message)s',
    datefmt='%Y-%b-%d %H:%M:%S',
    level=logging.INFO  # Set your desired log level here, e.g., logging.DEBUG
)
logger = logging.getLogger(__name__)
function_definitions = [
    {
        "name": "invoice",
        "description": "Get invoice information to extract values if not available value fill 'NA'",
        "parameters": {
            "type": "object",
            "properties": {
                "from": {
                    "type": "string",
                    "description": "Sender/bill to/shipper/owner of invoice Address of the invoice e.g. DEMO - Company Invoices, Plat 5A-1204, 123 Somewhere Street, Your City AZ 12345, abc@company.com"
                },
                "to": {
                    "type": "string",
                    "description": "Recipient/ship to/cosignee/ consumer of(Recipient) Address of the invoice e.g. DEMO - Company Invoices, Plat 5A-1204, 123 Somewhere Street, Your City AZ 12345, abc@company.com"
                },
                "invoice_name": {
                    "type": "string",
                    "description": "Unique identifier for the invoice name"
                },
                "invoice_number": {
                    "type": "string",
                    "description": "Unique identifier for the invoice number(no)"
                },
                "order_number": {
                    "type": "string",
                    "description": "Order number associated with the invoice number(no)"
                },
                "invoice_date": {
                    "type": "string",
                    "description": "Date of the invoice e.g. Jan 01, 2000 or 01/01/2000 or 01-01-2000"
                },
                "Contact for Sender": {
                    "type": "string",
                    "description": "contact for sender/billto/shipto/autherofinvoice of the invoice e.g. 'John'"
                },
                "Contact for Recipient": {
                    "type": "string",
                    "description": "contact for Recipient/cosignee/shipper/Recipient of invoice of the invoice e.g. 'John'"
                },
                "total": {
                    "type": "string",
                    "description": "Total amount in the invoice e.g. $100,€100,£100,¥100,₣100,₹100"
                },
                "invoice_status": {
                    "type": "string",
                    "description": "Status of the invoice e.g. 'paid' or 'pending'"
                },
                "invoice_payment": {
                    "type": "string",
                    "description": "Status of the invoice payment e.g. 'gpay','cash','online payment'"
                },
                "invoice_notes": {
                    "type": "string",
                    "description": "Additional notes or comments for the invoice"
                }
            },
            "required": ["from","Contact for Sender","to","Contact for Recipient", "invoice_number", "order_number", "invoice_date", "total","invoice_payment", "invoice_status","invoice_notes"]
        }
    }
]

template = """/
Scan the following invoice and return the match relevant details.
If the data is missing just return N/A
Invoice: {invoice}
"""

"""
Scan uploaded PDF or Word document to extract invoice details.
"""

def main():
    load_dotenv()

    llm = ChatOpenAI(model="gpt-3.5-turbo-0613")

    st.write("# Invoice Scanner")

    st.write("### Upload Your Invoice")

    status = st.empty()

    file = st.file_uploader("PDF, Word Doc", type=["pdf", "docx"])

    details = st.empty()

    if file is not None:
        with st.spinner("Scanning..."):
            text = ""
            if file.type == "application/pdf":
                with pdfplumber.open(file) as pdf:
                  text = ''
                  for page in pdf.pages:
                      text += page.extract_text()

            if file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                text += docx2txt.process(file)

            prompt = PromptTemplate.from_template(template)
            content = prompt.format(invoice=text)

            messages = [HumanMessage(content=content)]
            language_model = ChatOpenAI(model_name='gpt-4')

            try:
                message = language_model.predict_messages(
                    messages, functions=function_definitions)

                data = json.loads(
                    message.additional_kwargs["function_call"]["arguments"])
                logger.info('Extracted data: %s', data)

                st.header("Details")
                st.json(data)

                status = status.success("Invoice Scanned Successfully")
            except Exception as e:
                logger.exception("An error occurred: %s", str(e))
                st.error("An error occurred during processing.")


if __name__ == '__main__':
    main()
