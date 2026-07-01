import pandas as pd
import pdfplumber
import re


def parse_excel(file_path):
    df = pd.read_excel(file_path)
    return df.iloc[0].to_dict()


def parse_resume(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

    skills = list(set(re.findall(
        r'Python|Java|React|Node\.js|MongoDB|Streamlit|Git',
        text
    )))

    education = list(set(re.findall(
        r'Nitte Meenakshi Institute of Technology',
        text
    )))

    return {
        "skills": skills,
        "education": education
    }