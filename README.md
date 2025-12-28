# Resume–Job Matcher (Deterministic & Offline)

## 1. Problem Statement
Recruiters need a **consistent, explainable, and privacy-safe** way to compare resumes against job descriptions.
Manual screening is slow and subjective, while black-box AI tools introduce compliance and trust issues.

This project provides a **deterministic decision-support system** for resume matching.

---

## 2. Why NOT ChatGPT / GenAI
- Hiring decisions require **repeatable outputs**
- LLMs introduce randomness and hallucination risk
- External APIs raise **privacy, compliance, and cost** concerns
- This system must run **offline**

LLMs are powerful tools — but not replacements for classical ML systems in regulated workflows.

---

## 3. Architecture Overview

Resume Text ──┐
├─> Sentence Embeddings ─> Cosine Similarity ─> Match Score
Job Text ─────┘

Resume Text ──┐
├─> Rule-Based Skill Extraction ─> Skill Gap Analysis
Job Text ─────┘

---

## 4. Similarity Scoring
- Uses `sentence-transformers/all-MiniLM-L6-v2`
- Both texts embedded locally
- Cosine similarity computed
- Score scaled to **0–100%**
- Same input → same output (deterministic)

---

## 5. How to Run Locally

```bash
git clone <repo>
cd resume-matcher
pip install -r requirements.txt
streamlit run app.py
Then open: http://localhost:8501

6. Future Improvements
Skill weighting by seniority

Section-aware resume parsing

FAISS-based resume indexing

PDF/DOCX ingestion

Bias & fairness auditing metrics