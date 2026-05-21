import pandas as pd
import json
import sys
import os


def analyze_finances(file_path):
    # Load CSV safely
    df = pd.read_csv(file_path)

    # Build analysis output
    analysis = {
        "status": "success",
        "rows": int(len(df)),
        "columns": list(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "summary": df.describe(include="all").fillna("").to_dict()
    }

    # Ensure output path exists (safe for GitHub Actions)
    output_path = "backend/report.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write output report
    with open(output_path, "w") as f:
        json.dump(analysis, f, indent=2)

    print(f"Report generated successfully at {output_path}")

    return analysis


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: No CSV file provided")
        sys.exit(1)

    file_path = sys.argv[1]
    analyze_finances(file_path)
