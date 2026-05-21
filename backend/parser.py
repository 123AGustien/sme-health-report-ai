import pandas as pd

def parse_csv(file):
    df = pd.read_csv(file)

    # required columns
    required = ["date", "description", "amount", "type"]

    for col in required:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    # clean data
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"])

    df["type"] = df["type"].astype(str).str.lower().str.strip()

    df = df[df["type"].isin(["income", "expense"])]

    df["description"] = df["description"].astype(str).str.strip()

    return df
