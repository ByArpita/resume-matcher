# app.py

import streamlit as st
from matcher import compute_match_score
from skills import compute_skill_gap

st.set_page_config(
    page_title="Resume–Job Matcher",
    layout="centered"
)

st.title("📄 Resume–Job Matching System")
st.write(
    "A deterministic, offline decision-support tool for comparing resumes "
    "against job descriptions using local NLP models."
)

st.divider()

resume_text = st.text_area(
    "Paste Resume Text",
    height=250,
    placeholder="Paste the candidate's resume here..."
)

job_text = st.text_area(
    "Paste Job Description Text",
    height=250,
    placeholder="Paste the job description here..."
)

if st.button("Run Matching"):
    if not resume_text.strip() or not job_text.strip():
        st.warning("Please provide both resume and job description text.")
    else:
        score = compute_match_score(resume_text, job_text)
        missing_skills = compute_skill_gap(resume_text, job_text)

        st.subheader("📊 Match Results")
        st.metric(label="Match Score", value=f"{score:.2f}%")

        st.subheader("🧩 Missing Skills")
        if missing_skills:
            for skill in missing_skills:
                st.write(f"- {skill}")
        else:
            st.write("No missing skills detected.")
