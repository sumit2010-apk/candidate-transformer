import re


def normalize_phone(phone):
    digits = re.sub(r'\D', '', str(phone))

    if len(digits) == 10:
        return "+91" + digits

    return digits


def normalize_skills(skills):
    return [skill.lower().strip() for skill in skills]