import io
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_bytes):
    pdf_stream = io.BytesIO(pdf_bytes)
    reader = PdfReader(pdf_stream)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
