def generate_insights(df):
    """
    Simple SME business insights engine (MVP version)
    """

    insights = []

    # 1. Basic size check
    if len(df) > 50:
        insights.append("High transaction volume detected")

    # 2. Look for amount column
    if "amount" in df.columns:
        avg = df["amount"].mean()
        insights.append(f"Average transaction value: {round(avg, 2)}")

    # 3. Cashflow warning logic (simple rule)
    if "amount" in df.columns:
        total = df["amount"].sum()
        if total < 0:
            insights.append("Warning: Negative cashflow detected")

    # 4. Default advisory
    insights.append("Recommendation: Monitor weekly cashflow and overdue invoices")

    return insights
