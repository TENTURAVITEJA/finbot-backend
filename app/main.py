from fastapi import FastAPI, UploadFile, File, HTTPException
from app.utils import parse_pdf_and_categorize
from app.models import FinancialSummary

@app.post("/analyze", response_model=FinancialSummary)
async def analyze_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    result = await parse_pdf_and_categorize(file)
    return result
