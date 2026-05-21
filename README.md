sme-health-report-ai

AI-powered SME financial intelligence system that generates business health reports from financial data.

---

Overview

"sme-health-report-ai" is a lightweight SaaS prototype designed to help SMEs, startups, and operators understand business financial health through automated analysis.

The platform converts uploaded financial data into simplified operational intelligence including:

- revenue analysis
- expense tracking
- net cashflow calculation
- risk scoring
- downloadable business reports

---

Vision

Traditional accounting platforms focus on bookkeeping and compliance.

This project focuses on:

«simple financial visibility and business decision intelligence for SMEs.»

The goal is to reduce accounting complexity and provide fast operational insights for non-accountants.

---

Current Features

- CSV financial data ingestion
- Python-based financial analysis engine
- GitHub Actions workflow automation
- downloadable JSON business reports
- lightweight HTML dashboard
- offline simulation mode

---

Example Workflow

CSV Upload
    ↓
AI Analysis Engine
    ↓
Risk + Cashflow Analysis
    ↓
JSON Report Generation
    ↓
Downloadable Report Artifact

---

Example Report Output

{
  "status": "processed",
  "total_revenue": 4500,
  "total_expense": 2000,
  "net_cashflow": 2500,
  "risk_level": "LOW"
}

---

Repository Structure

sme-health-report-ai/
│
├── index.html
├── sample.csv
├── backend/
│   ├── ai_engine.py
│   ├── parser.py
│   └── report_generator.py
│
└── .github/workflows/
    ├── manual-test.yml
    └── sextant-ai.yml

---

Technology Stack

- Python
- Pandas
- GitHub Actions
- HTML / JavaScript
- JSON reporting

---

Future Roadmap

- Xero integration
- QuickBooks integration
- Google Sheets sync
- AI financial recommendations
- live dashboard analytics
- automated scheduled reporting
- cloud SaaS deployment

---

Product Positioning

This project is NOT accounting software.

It is designed as:

«an AI-powered business health intelligence layer for SMEs.»

The focus is:

- simplicity
- operational visibility
- decision support
- financial awareness

---

Status

Prototype / experimental SaaS architecture under active development.

---

Author

Don Herman Oswald Weerasekera
Founder – Sextant Protocol
