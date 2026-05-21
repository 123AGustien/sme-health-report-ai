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
      # 1. Checkout repo
      - name: Checkout repo
        uses: actions/checkout@v4

      # 2. Setup Python
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      # 3. Install dependencies
      - name: Install dependencies
        run: |
          pip install pandas openai

      # 4. Run engine
      - name: Run Sextant Engine
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          python backend/engine.py "${{ github.event.inputs.file }}"

      # 5. DEBUG STEP (VERY IMPORTANT)
      - name: Check output files
        run: |
          ls -R

      # 6. Upload report
      - name: Upload Report (Downloadable Output)
        uses: actions/upload-artifact@v4
        with:
          name: sme-business-report
          path: backend/report.json
