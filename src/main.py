from parser import parse_excel, parse_resume
from merger import merge_data
from validator import validate_json
import json


excel_data = parse_excel("input/data_v1.xlsx")
resume_data = parse_resume("input/sumitresume.pdf")

final_data = merge_data(excel_data, resume_data)

validate_json(final_data)

with open("output.json", "w") as f:
    json.dump(final_data, f, indent=4)

print("Transformation completed!")