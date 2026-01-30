def explain_clause(risk_level: str) -> str:
    if risk_level == "High":
        return (
            "This clause may expose your business to significant legal or "
            "financial risk. Consider renegotiating or limiting liability."
        )

    if risk_level == "Medium":
        return (
            "This clause creates obligations that should be clearly "
            "understood and managed."
        )

    return "This clause is generally balanced and commonly used."


def generate_summary(clauses: list, entities: dict, risk: str) -> str:
    return (
        f"Overall Contract Risk: {risk}\n\n"
        f"Total Clauses Analyzed: {len(clauses)}\n"
        f"Dates Identified: {', '.join(entities.get('dates', [])) or 'None'}\n"
        f"Amounts Mentioned: {', '.join(entities.get('amounts', [])) or 'None'}\n\n"
        "Recommendation:\n"
        "Review high-risk clauses carefully and consult a legal professional "
        "before signing."
    )
