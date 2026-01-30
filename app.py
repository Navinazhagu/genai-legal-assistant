import streamlit as st
import hashlib
import json
from datetime import datetime

from legal_nlp.file_reader import read_contract
from legal_nlp.clause_extraction import extract_clauses
from legal_nlp.ner import extract_entities
from legal_nlp.risk_engine import assess_clause_risk, calculate_overall_risk
from legal_nlp.summarizer import explain_clause, generate_summary

# ---------------- CONFIG ---------------- #
st.set_page_config(
    page_title="GenAI Legal Assistant",
    layout="wide"
)

st.title("GenAI-Powered Legal Assistant for SMEs")
st.caption("Understand contracts, identify risks, take action")

st.info(
    "Confidentiality Notice: All analysis is performed locally. "
    "This tool assists understanding and does not replace legal advice."
)

# ---------------- FILE UPLOAD ---------------- #
uploaded_file = st.file_uploader(
    "Upload a contract (PDF, DOCX, TXT)",
    type=["pdf", "docx", "txt"]
)

if not uploaded_file:
    st.stop()

# ---------------- PROCESSING ---------------- #
contract_text = read_contract(uploaded_file)
document_id = hashlib.sha256(contract_text.encode()).hexdigest()[:10]

clauses = extract_clauses(contract_text)
entities = extract_entities(contract_text)

analysis_results = []

for clause in clauses:
    risk = assess_clause_risk(clause["text"])
    explanation = explain_clause(risk)

    analysis_results.append({
        "id": clause["id"],
        "title": clause["title"],
        "text": clause["text"],
        "risk": risk,
        "explanation": explanation
    })

overall_risk = calculate_overall_risk([c["risk"] for c in analysis_results])
summary = generate_summary(analysis_results, entities, overall_risk)

# ---------------- UI OUTPUT ---------------- #
st.subheader("Overall Contract Risk")
risk_labels = {
    "High": "High Risk",
    "Medium": "Medium Risk",
    "Low": "Low Risk"
}
st.markdown(f"### {risk_labels[overall_risk]}")

st.subheader("Simplified Contract Summary")
st.write(summary)

st.subheader("Clause-by-Clause Analysis")

for clause in analysis_results:
    with st.expander(f"{clause['id']} — {clause['risk']} Risk"):
        st.write("Clause Text:")
        st.write(clause["text"])
        st.write("Explanation:")
        st.write(clause["explanation"])

# ---------------- AUDIT LOG ---------------- #
audit_entry = {
    "document_id": document_id,
    "timestamp": datetime.utcnow().isoformat(),
    "action": "contract_analysis"
}

with open("audit_logs/audit.json", "a") as log:
    log.write(json.dumps(audit_entry) + "\n")

# ---------------- EXPORT ---------------- #
st.download_button(
    label="Download Summary",
    data=summary,
    file_name="contract_summary.txt"
)
