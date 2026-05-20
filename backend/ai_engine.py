import os
from openai import OpenAI

# Load API key securely from environment variable
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_insights(df):
    """
    Uses GPT to generate SME business insights
    """

    # Convert first rows into readable text
    data_preview = df.head(10).to_string()

    prompt = f"""
    You are an SME financial advisor.

    Analyze this business transaction data and provide:

    1. Cashflow observations
    2. Risks
    3. Recommendations
    4. Weekly business health summary

    Data:
    {data_preview}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    insights = response.choices[0].message.content

    return insights
