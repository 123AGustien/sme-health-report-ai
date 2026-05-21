from flask import Flask, jsonify, request
from backend.parser import parse_csv
from backend.ai_engine import analyze_finances
from backend.report_generator import generate_report

app = Flask(__name__)

app.secret_key = "sme-ai-v4-secret"

# =========================
# HEALTH CHECK
# =========================
@app.route("/")
def home():
    return {
        "status": "SME AI SaaS v4 LIVE",
        "message": "Upload CSV to /upload for full analysis"
    }

# =========================
# FULL SAAS PIPELINE
# =========================
@app.route("/upload", methods=["POST"])
def upload():
    try:
        file = request.files.get("file")

        if not file:
            return jsonify({"error": "No file uploaded"}), 400

        # 1. PARSE
        df = parse_csv(file)

        # 2. AI ANALYSIS
        ai_result = analyze_finances(df)

        # 3. REPORT GENERATION
        report = generate_report(ai_result, df)

        # FINAL OUTPUT (SAAS RESPONSE)
        return jsonify({
            "status": "success",
            "ai_result": ai_result,
            "report": report
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)
