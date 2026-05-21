name: Sextant AI CSV Engine

on:
  workflow_dispatch:
    inputs:
      file:
        description: "CSV file name in repo"
        required: true

jobs:
  run-engine:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          pip install pandas openai

      - name: Run Sextant Engine
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          python backend/engine.py "${{ github.event.inputs.file }}"

      - name: Upload Report (Downloadable Output)
        uses: actions/upload-artifact@v4
        with:
          name: sme-business-report
          path: report.json
