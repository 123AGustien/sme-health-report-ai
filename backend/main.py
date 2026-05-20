from fastapi import FastAPI, UploadFile, File
import pandas as pd
from backend.parser import parse_file
from backend.ai_engine import generate_insights

app = FastAPI()

@app.get("/")
def home():
    return {"status": "SME Health AI MVP running"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    contents = await file.read()

    df = parse_file(contents)

    insights = generate_insights(df)

    return {
        "rows": len(df),
        "columns": list(df.columns),
        "insights": insights
    }
