import jsonschema


schema = {
    "type": "object",
    "properties": {
        "candidate_id": {"type": "string"},
        "profile": {"type": "object"},
        "academic_scores": {"type": "object"},
        "technical_assessment": {"type": "object"},
        "resume_extracted": {"type": "object"},
        "overall_confidence": {"type": "number"}
    },
    "required": [
        "candidate_id",
        "profile",
        "technical_assessment",
        "resume_extracted",
        "overall_confidence"
    ]
}


def validate_json(data):
    jsonschema.validate(instance=data, schema=schema)
    print("JSON validation successful!")