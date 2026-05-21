def analyze_finances(df):
    # ensure numeric safety
    df["amount"] = df["amount"].fillna(0)

    # =========================
    # CORE METRICS
    # =========================
    income = df[df["type"] == "income"]["amount"].sum()
    expense = df[df["type"] == "expense"]["amount"].sum()
    net = income + expense

    # =========================
    # RISK ENGINE
    # =========================
    if net < 0:
        risk = "HIGH"
    elif expense > income * 0.7:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    # =========================
    # AI SUMMARY ENGINE
    # =========================
    if net > 0:
        summary = "Your business is profitable. Cashflow is positive."
    elif net == 0:
        summary = "Your business is breaking even. No profit detected."
    else:
        summary = "Your business is losing money. Expenses exceed income."

    # =========================
    # INSIGHT ENGINE
    # =========================
    expense_df = df[df["type"] == "expense"].sort_values("amount")

    biggest_expense = None
    if not expense_df.empty:
        biggest_expense = expense_df.head(1).to_dict(orient="records")

    # =========================
    # OUTPUT (SaaS API FORMAT)
    # =========================
    return {
        "total_income": float(income),
        "total_expense": float(expense),
        "net_cashflow": float(net),
        "risk_level": risk,
        "ai_summary": summary,
        "biggest_expense": biggest_expense,
        "rows": len(df)
    }
