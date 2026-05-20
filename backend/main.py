from fastapi import FastAPI, UploadFile, File
from backend.parser import parse_file
from backend.ai_engine import generate_insights
from backend.report_generator import generate_report

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "SME Health AI MVP running"
    }

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        # Read uploaded file
        contents = await file.read()

        # Parse Excel data
        df = parse_file(contents)

        # Generate business insights
        insights = generate_insights(df)

        # Generate formatted report
        report = generate_report(insights)

        return {
            "status": "success",
            "rows_processed": len(df),
            "columns": list(df.columns),
            "report": report
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
