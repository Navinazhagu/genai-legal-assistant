HIGH_RISK_TERMS = [
    "penalty",
    "indemnify",
    "terminate at any time",
    "non-compete",
    "unlimited liability",
    "exclusive"
]

MEDIUM_RISK_TERMS = [
    "shall",
    "must",
    "binding",
    "auto renew",
    "lock-in",
    "arbitration"
]


def assess_clause_risk(text: str) -> str:
    content = text.lower()

    if any(term in content for term in HIGH_RISK_TERMS):
        return "High"

    if any(term in content for term in MEDIUM_RISK_TERMS):
        return "Medium"

    return "Low"


def calculate_overall_risk(risks: list) -> str:
    if "High" in risks:
        return "High"
    if "Medium" in risks:
        return "Medium"
    return "Low"
