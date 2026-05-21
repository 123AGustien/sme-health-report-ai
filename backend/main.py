from flask import Flask, jsonify, request
from backend.parser import parse_csv
from backend.ai_engine import analyze_finances

app = Flask(__name__)

app.secret_key = "sme-ai-v4-secret"

# =========================
# HOME
# =========================
@app.route("/")
def home():
    return {
        "status": "SME AI SaaS v4 running",
        "message": "Upload CSV to /upload"
    }

# =========================
# UPLOAD CSV
# =========================
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    df = parse_csv(file)
    result = analyze_finances(df)

    return jsonify(result)


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)
