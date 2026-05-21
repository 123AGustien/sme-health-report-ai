from backend.parser import parse_csv
from backend.ai_engine import analyze_finances
from backend.report_generator import generate_report
import pandas as pd
from io import StringIO

def test_full_pipeline():

    csv_data = """date,description,amount,type
2026-05-01,sales,5000,income
2026-05-02,rent,-1500,expense
2026-05-03,ads,-300,expense
"""

    df = pd.read_csv(StringIO(csv_data))

    # run pipeline
    ai = analyze_finances(df)
    report = generate_report(ai, df)

    print("AI RESULT:", ai)
    print("REPORT:", report)

    assert ai["net_cashflow"] == 3200
    assert ai["risk_level"] in ["LOW", "MEDIUM", "HIGH"]

if __name__ == "__main__":
    test_full_pipeline()
