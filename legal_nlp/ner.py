import re


def extract_entities(text: str) -> dict:
    return {
        "dates": re.findall(r"\b\d{1,2}/\d{1,2}/\d{4}\b", text),
        "amounts": re.findall(r"₹\s?\d+[,\d]*", text),
        "jurisdiction": re.findall(
            r"India|Tamil Nadu|Karnataka|Delhi", text, re.IGNORECASE
        )
    }
