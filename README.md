# Candidate Transformer
# Candidate Transformer

## Overview
This project transforms structured and unstructured candidate data into a unified canonical profile.

## Sources
- Structured: Excel file
- Unstructured: Resume PDF

## Run
pip install pandas pdfplumber jsonschema openpyxl

python src/main.py

## Output
Generates output.json with:
- profile
- academic scores
- technical assessment
- extracted skills
- provenance
- confidence score

## Run

pip install -r requirements.txt

python src/main.py
