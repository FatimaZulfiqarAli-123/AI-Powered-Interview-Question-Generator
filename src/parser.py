
import re


def extract_sections(text):

    technical = ""
    behavioral = ""

    technical_match = re.search(
        r"TECHNICAL QUESTIONS(.*?)(?:BEHAVIORAL QUESTIONS|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    behavioral_match = re.search(
        r"BEHAVIORAL QUESTIONS(.*)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if technical_match:

        technical = technical_match.group(1).strip()

    if behavioral_match:

        behavioral = behavioral_match.group(1).strip()

    return {
        "technical": technical,
        "behavioral": behavioral
    }