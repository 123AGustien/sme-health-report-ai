import pandas as pd
import sys
import json
import os

# Optional OpenAI (safe fallback if no key)
try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    USE_AI = True
except:
    USE_AI = False


file = sys.argv[1]

df = pd.read_csv(file)

revenue = df["revenue"].sum() if "revenue" in df else 0
expense = df["expense"].sum() if "expense" in df else 0

net = revenue - expense

risk = "LOW"
if net < 0:
    risk = "HIGH"
elif expense > revenue * 0.7:
    risk = "MEDIUM"


# ---------------------------
# OPENAI INSIGHT LAYER
# ---------------------------
ai_insight = "AI not enabled"

if USE_AI:
    prompt = f"""
    Analyze this SME financial data:
    Revenue: {revenue}
    Expense: {expense}
    Net: {net}
    Risk: {risk}

    Give a short business insight and recommendation.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    ai_insight = response.choices[0].message.content


# ---------------------------
# FINAL REPORT
# ---------------------------
report = {
    "rows": len(df),
    "total_revenue": float(revenue),
    "total_expense": float(expense),
    "net_cashflow": float(net),
    "risk_level": risk,
    "ai_insight": ai_insight,
    "status": "processed via Sextant Engine"
}

# Save output file
with open("report.json", "w") as f:
    json.dump(report, f, indent=2)

print(json.dumps(report, indent=2))
