from datetime import datetime

def generate_report(ai_result, df):

    net = ai_result["net_cashflow"]

    if net > 5000:
        health = "EXCELLENT"
    elif net > 0:
        health = "GOOD"
    elif net == 0:
        health = "STABLE"
    else:
        health = "CRITICAL"

    return {
        "generated_at": datetime.now().isoformat(),
        "total_transactions": len(df),

        "financial_summary": {
            "income": ai_result["total_income"],
            "expense": ai_result["total_expense"],
            "net": ai_result["net_cashflow"]
        },

        "ai_insight": {
            "risk_level": ai_result["risk_level"],
            "summary": ai_result["ai_summary"]
        },

        "business_health": health,

        "key_insights": {
            "biggest_expense": ai_result["biggest_expense"]
        }
    }
