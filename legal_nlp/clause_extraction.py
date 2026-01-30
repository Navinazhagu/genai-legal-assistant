import re


def extract_clauses(text: str) -> list:
    raw_clauses = re.split(r"\n\s*\d+[\.\)]\s*", text)

    clauses = []
    for index, clause in enumerate(raw_clauses, start=1):
        cleaned = clause.strip()
        if len(cleaned) > 50:
            clauses.append({
                "id": f"Clause {index}",
                "title": "General",
                "text": cleaned
            })

    return clauses
