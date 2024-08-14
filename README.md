# OpenAI Function Calling Custom Document and Invoice

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![OpenAI](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![Kali](https://img.shields.io/badge/Kali-268BEE?style=for-the-badge&logo=kalilinux&logoColor=white)![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)![Google](https://img.shields.io/badge/google-4285F4?style=for-the-badge&logo=google&logoColor=white)![DuckDuckGo](https://img.shields.io/badge/DuckDuckGo-DE5833?style=for-the-badge&logo=DuckDuckGo&logoColor=white)![Edge](https://img.shields.io/badge/Microsoft%20Edge-0078D7.svg?style=for-the-badge&logo=Microsoft-Edge&logoColor=white)![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white)![Open Project](https://img.shields.io/badge/OpenProject-0770B8.svg?style=for-the-badge&logo=OpenProject&logoColor=white)![Open Access](https://img.shields.io/badge/Open%20Access-F68212.svg?style=for-the-badge&logo=Open-Access&logoColor=white)

# **Let's connect :**

[![GitHub](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/karthikeyanrathinam/)
[![Linkedin](https://img.shields.io/badge/LinkedIn-0A66C2.svg?style=for-the-badge&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/karthikeyanrathinam/)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@linkagethink)
[![Gmail](https://img.shields.io/badge/Gmail-EA4335.svg?style=for-the-badge&logo=Gmail&logoColor=white)](mailto:karthikeyanr1801@gmail.com)
# Invoice/Document's Scanner for LLM Function calling using OpenAI Streamlit Webapp

This project implements an invoice scanner using OpenAI's language model. The scanner extracts relevant details from uploaded PDF or Word documents, such as invoice number, date, total amount, and more.

## **Table of Contents**
- [Installation](#installation)
- [Usage](#usage)
- [Function Definitions](#function-definitions)
- [Contributing](#contributing)
- [License](#license)

## **Installation**

Use the following commands to set up the project:

```bash
pip install -r requirements.txt
npm install localtunnel
```


Create a .env file and add your OpenAI API key
```python
OPENAI_API_KEY="Your API Key"
```
or 
Set Local Variable If needed
```python
import os
os.environ['OPENAI_API_KEY']='sk-......................'
```

## **Usage**
Run the application locally using the following command:

```bash
streamlit run app.py
```

This will start a local server. Open your browser and go to http://localhost:8501 to access the Invoice Scanner.


For Colab, use the following commands:
```bash
!streamlit run app.py &>/content/logs.txt & npx localtunnel --port 8501 & curl ipv4.icanhazip.com
```
Copy ipv4 ip paste localtunnel page

## **Function Definitions**
The project includes predefined functions for handling different types of invoices. Here's an example function definition:

```python
{
  "name": "invoice",
  "description": "Get invoice information to extract values if not available value fill 'NA'",
  "parameters": {
    // ... (see provided code for detailed parameters)
  },
  "required": ["from", "Contact for Sender", "to", "Contact for Recipient", "invoice_number", "order_number", "invoice_date", "total", "invoice_payment", "invoice_status", "invoice_notes"]
}

```

## **Contributing**
Contributions to this project are welcome! If you'd like to contribute, please open an issue or submit a pull request.

## **License**
This project is licensed under the MIT License.

Feel free to reach out if you have any questions or need further assistance.

## **Follow**

[![GitHub](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/karthikeyanrathinam/)
[![Linkedin](https://img.shields.io/badge/LinkedIn-0A66C2.svg?style=for-the-badge&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/karthikeyanrathinam/)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@linkagethink)
[![Gmail](https://img.shields.io/badge/Gmail-EA4335.svg?style=for-the-badge&logo=Gmail&logoColor=white)](mailto:karthikeyanr1801@gmail.com)

