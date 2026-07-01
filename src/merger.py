import math


def calculate_confidence(field, source):
    confidence_map = {
        "excel": 0.95,
        "resume": 0.85
    }
    return confidence_map.get(source, 0.50)


def clean_nan(value):
    if isinstance(value, float) and math.isnan(value):
        return None
    return value


def merge_data(excel_data, resume_data):
    final_data = {
        "candidate_id": str(excel_data.get("Application_ID")),

        "profile": {
            "current_city": excel_data.get("Current City"),
            "degree": excel_data.get("Degree"),
            "stream": excel_data.get("Stream"),
            "graduation_year": excel_data.get("Current Year Of Graduation")
        },

        "academic_scores": {
            "ug": clean_nan(excel_data.get("Performance_UG")),
            "class_12": clean_nan(excel_data.get("Performance_12")),
            "class_10": clean_nan(excel_data.get("Performance_10"))
        },

        "technical_assessment": {
            "python": {
                "score": excel_data.get("Python (out of 3)"),
                "confidence": calculate_confidence("python", "excel"),
                "source": "excel"
            },
            "r_programming": {
                "score": excel_data.get("R Programming (out of 3)"),
                "confidence": calculate_confidence("r_programming", "excel"),
                "source": "excel"
            },
            "deep_learning": {
                "score": excel_data.get("Deep Learning (out of 3)"),
                "confidence": calculate_confidence("deep_learning", "excel"),
                "source": "excel"
            },
            "mongodb": {
                "score": excel_data.get("MongoDB (out of 3)"),
                "confidence": calculate_confidence("mongodb", "excel"),
                "source": "excel"
            },
            "nodejs": {
                "score": excel_data.get("Node.js (out of 3)"),
                "confidence": calculate_confidence("nodejs", "excel"),
                "source": "excel"
            },
            "reactjs": {
                "score": excel_data.get("ReactJS (out of 3)"),
                "confidence": calculate_confidence("reactjs", "excel"),
                "source": "excel"
            }
        },

        "resume_extracted": {
            "skills": [
                {
                    "name": skill,
                    "confidence": calculate_confidence(skill, "resume"),
                    "source": "resume"
                }
                for skill in resume_data.get("skills", [])
            ],
            "education": [
                {
                    "name": edu,
                    "confidence": calculate_confidence(edu, "resume"),
                    "source": "resume"
                }
                for edu in resume_data.get("education", [])
            ]
        },

        "provenance": [
            {
                "field": "technical_assessment",
                "source": "excel"
            },
            {
                "field": "resume_extracted",
                "source": "resume"
            }
        ],

        "overall_confidence": round(
            (
                calculate_confidence("excel_data", "excel") +
                calculate_confidence("resume_data", "resume")
            ) / 2,
            2
        )
    }

    return final_data