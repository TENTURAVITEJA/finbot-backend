from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from app.utils import extract_text_from_pdf
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FinBot PDF Analyzer is running!"}

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        text = extract_text_from_pdf(contents)
        return JSONResponse(content={"extracted_text": text})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# Run the app using uvicorn
# Run from terminal: uvicorn app.main:app --reload
