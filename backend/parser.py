import pandas as pd

def parse_csv(file):
    """
    SaaS-safe CSV parser for SME AI system.
    Cleans and validates financial data before AI processing.
    """

    # =========================
    # LOAD CSV
    # =========================
    df = pd.read_csv(file)

    # =========================
    # REQUIRED COLUMNS CHECK
    # =========================
    required_columns = ["date", "description", "amount", "type"]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # =========================
    # CLEAN DATA
    # =========================
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"])

    df["type"] = df["type"].astype(str).str.lower().str.strip()

    # =========================
    # VALIDATE TYPE VALUES
    # =========================
    valid_types = ["income", "expense"]
    df = df[df["type"].isin(valid_types)]

    # =========================
    # CLEAN TEXT FIELDS
    # =========================
    df["description"] = df["description"].astype(str).str.strip()

    # =========================
    # RETURN CLEAN DATAFRAME
    # =========================
    return df
