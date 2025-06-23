import PyPDF2
import docx

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    return " ".join([page.extract_text() for page in reader.pages])

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return " ".join([para.text for para in doc.paragraphs])

def extract_resume_text(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)
    else:
        return "Unsupported file format"
