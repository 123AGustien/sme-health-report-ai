from datetime import datetime

def generate_report(ai_result, df):
    """
    Converts AI engine output into a structured SaaS business report.
    This is what your dashboard or future PDF/email system will use.
    """

    # =========================
    # BASIC INFO
    # =========================
    report = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_transactions": len(df),

        # =========================
        # FINANCIAL SUMMARY
        # =========================
        "financial_summary": {
            "income": ai_result["total_income"],
            "expense": ai_result["total_expense"],
            "net_cashflow": ai_result["net_cashflow"]
        },

        # =========================
        # AI INSIGHTS
        # =========================
        "ai_insight": {
            "risk_level": ai_result["risk_level"],
            "summary": ai_result["ai_summary"]
        },

        # =========================
        # DETAIL INSIGHT
        # =========================
        "key_insights": []
    }

    # =========================
    # ADD INSIGHTS
    # =========================
    if ai_result["biggest_expense"]:
        report["key_insights"].append({
            "type": "biggest_expense",
            "data": ai_result["biggest_expense"]
        })

    # =========================
    # HEALTH SCORE (SIMPLE SaaS METRIC)
    # =========================
    net = ai_result["net_cashflow"]

    if net > 5000:
        health_score = "EXCELLENT"
    elif net > 0:
        health_score = "GOOD"
    elif net == 0:
        health_score = "STABLE"
    else:
        health_score = "CRITICAL"

    report["business_health"] = health_score

    return report
