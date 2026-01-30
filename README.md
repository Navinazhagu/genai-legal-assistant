**GenAI-Powered Legal Assistant for SMEs**
**Overview**
Small and medium businesses often sign legal contracts without fully understanding the terms and risks involved. Legal documents are complex, time-consuming to review, and professional legal help is not always affordable.
This project is a GenAI-powered legal assistant that helps business owners understand contracts in plain language, identify risky clauses, and make better decisions before signing.

**What This Project Does**
Allows users to upload contracts in PDF, DOCX, or TXT format
Breaks the contract into individual clauses
Explains each clause in simple business language
Identifies risky or unfavorable terms
Provides an overall risk level for the contract
Generates a short summary that can be downloaded
Keeps all processing local to maintain confidentiality

**Why This Is Useful**
This tool is designed especially for Indian small and medium businesses who may not have access to frequent legal consultation. It helps users quickly understand important contract terms and spot potential problems early.

**Technology Used**

Python
Streamlit for the web interface
Rule-based NLP for clause extraction and risk analysis
Local file processing with audit logs

**How to Run the Project Locally**
pip install -r requirements.txt
streamlit run app.py

**Disclaimer**
This application is intended to assist with contract understanding and risk awareness. It does not replace professional legal advice.

