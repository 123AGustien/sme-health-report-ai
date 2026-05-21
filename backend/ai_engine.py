import pandas as pd
import json
import sys

def analyze_finances(file_path):
    # Load CSV
    df = pd.read_csv(file_path)

    # Basic analysis (safe + stable MVP)
    analysis = {
        "status": "success",
        "rows": int(len(df)),
        "columns": list(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "summary": df.describe(include="all").to_dict()
    }

    # Save report
    output_path = "backend/report.json"
    with open(output_path, "w") as f:
        json.dump(analysis, f, indent=2)

    return analysis


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: No CSV file provided")
        sys.exit(1)

    file_path = sys.argv[1]
    analyze_finances(file_path)
    print("Report generated successfully")
