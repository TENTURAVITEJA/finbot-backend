import pdfplumber
import pandas as pd
import io
from fastapi import UploadFile
from app.models import FinancialSummary

CATEGORY_KEYWORDS = {
    "Groceries": ["supermarket", "grocery", "big bazaar", "dmart"],
    "Food": ["zomato", "swiggy", "restaurant", "cafe"],
    "Travel": ["uber", "ola", "flight", "train", "airlines"],
    "Utilities": ["electricity", "water", "internet", "mobile"],
    "Entertainment": ["netflix", "prime", "hotstar", "spotify"],
    "Shopping": ["amazon", "flipkart", "myntra"]
}

async def parse_pdf_and_categorize(file: UploadFile) -> FinancialSummary:
    content = await file.read()
    pdf = pdfplumber.open(io.BytesIO(content))

    transactions = []
    for page in pdf.pages:
        text = page.extract_text()
        lines = text.split('\n')
        for line in lines:
            if any(char.isdigit() for char in line):
                transactions.append(line.lower())

    pdf.close()

    df = pd.DataFrame(transactions, columns=["raw"])
    df["amount"] = df["raw"].str.extract(r'(\d+\.\d{2})').astype(float)
    df = df.dropna(subset=["amount"])

    def get_category(row):
        for category, keywords in CATEGORY_KEYWORDS.items():
            if any(keyword in row["raw"] for keyword in keywords):
                return category
        return "Others"

    df["category"] = df.apply(get_category, axis=1)
    grouped = df.groupby("category")["amount"].sum().to_dict()
    total_spent = df["amount"].sum()

    # Suggestion logic
    top_category = max(grouped, key=grouped.get, default="None")
    suggestion = f"Try reducing spend in '{top_category}' to save more."

    return FinancialSummary(
        total_spent=round(total_spent, 2),
        category_wise_spending={k: round(v, 2) for k, v in grouped.items()},
        suggestions=suggestion
    )
