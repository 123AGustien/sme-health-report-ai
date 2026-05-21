from fastapi import FastAPI, UploadFile, File
import pandas as pd

from backend.parser import parse_csv
from backend.ai_engine import analyze_finances
from backend.report_generator import generate_report

app = FastAPI(title="SME AI SaaS v4 (FastAPI)")

# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def home():
    return {
        "status": "SME AI FastAPI running",
        "version": "v4"
    }

# =========================
# UPLOAD CSV + FULL PIPELINE
# =========================
@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    # 1. LOAD CSV
    df = parse_csv(file.file)

    # 2. AI ANALYSIS
    ai_result = analyze_finances(df)

    # 3. REPORT GENERATION
    report = generate_report(ai_result, df)

    # FINAL RESPONSE
    return {
        "status": "success",
        "ai_result": ai_result,
        "report": report
    }
