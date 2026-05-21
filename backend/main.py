from fastapi import FastAPI, UploadFile, File
import pandas as pd

from backend.parser import parse_csv
from backend.ai_engine import analyze_finances
from backend.report_generator import generate_report

app = FastAPI(title="SME AI SaaS v4")

# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def home():
    return {
        "status": "SME AI FastAPI running",
        "version": "v4",
        "docs": "/docs"
    }


# =========================
# UPLOAD CSV + FULL SAAS PIPELINE
# =========================
@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    try:
        # =========================
        # 1. PARSE CSV (CLEAN DATA)
        # =========================
        df = parse_csv(file.file)

        # =========================
        # 2. AI FINANCIAL ENGINE
        # =========================
        ai_result = analyze_finances(df)

        # =========================
        # 3. REPORT GENERATOR
        # =========================
        report = generate_report(ai_result, df)

        # =========================
        # FINAL RESPONSE (SAAS API)
        # =========================
        return {
            "status": "success",
            "rows": len(df),
            "ai_result": ai_result,
            "report": report
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
