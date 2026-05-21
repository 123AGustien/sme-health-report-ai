import pandas as pd
import json
import sys
import os

def analyze_finances(file_path):
    df = pd.read_csv(file_path)

    analysis = {
        "status": "success",
        "rows": int(len(df)),
        "columns": list(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "summary": df.describe(include="all").to_dict()
    }

    # Ensure folder exists (VERY IMPORTANT in GitHub Actions)
    os.makedirs("backend", exist_ok=True)

    output_path = "backend/report.json"
    with open(output_path, "w") as f:
        json.dump(analysis, f, indent=2)

    print("Report generated at:", output_path)

    return analysis


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: No CSV file provided")
        sys.exit(1)

    analyze_finances(sys.argv[1])
