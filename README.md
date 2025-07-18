# FinBot – Financial Planner API

This backend receives credit card statements (PDF), extracts expenses, categorizes them using ML-like logic, and returns financial insights.

## Features
- Upload PDF statements
- Categorize expenses (Food, Travel, etc.)
- Get total and category-wise spend
- Receive suggestions

## Tech Stack
- FastAPI
- Python
- pdfplumber
- pandas

## Endpoint
- POST `/analyze` — Upload PDF and get analysis

