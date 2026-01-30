import pdfplumber
from docx import Document


def read_contract(uploaded_file) -> str:
    filename = uploaded_file.name.lower()

    if filename.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    if filename.endswith(".pdf"):
        with pdfplumber.open(uploaded_file) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)

    if filename.endswith(".docx"):
        document = Document(uploaded_file)
        return "\n".join(p.text for p in document.paragraphs)

    raise ValueError("Unsupported file format")
