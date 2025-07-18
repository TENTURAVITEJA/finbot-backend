from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Request model for WhatsApp upload (e.g., PDF)
class FileUploadRequest(BaseModel):
    user_id: str
    file_name: str
    uploaded_at: Optional[datetime] = None

# Output: extracted transactions from PDF
class Transaction(BaseModel):
    date: datetime
    description: str
    amount: float
    category: Optional[str] = "Uncategorized"

class FinancialSummary(BaseModel):
    total_income: float
    total_expense: float
    net_savings: float
    top_categories: List[str]

class FinancialReportResponse(BaseModel):
    user_id: str
    generated_at: datetime
    summary: FinancialSummary
    transactions: List[Transaction]
