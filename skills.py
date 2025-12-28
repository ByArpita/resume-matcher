# skills.py

import re
from typing import List, Set

# Predefined, auditable skill vocabulary
SKILL_LIST = {
    "python", "java", "sql", "javascript", "typescript",
    "machine learning", "deep learning", "nlp",
    "data analysis", "data science",
    "pandas", "numpy", "scikit-learn",
    "tensorflow", "pytorch",
    "docker", "kubernetes",
    "aws", "gcp", "azure",
    "linux", "git", "rest api",
    "streamlit", "flask", "fastapi"
}


def normalize_text(text: str) -> str:
    """Lowercase and remove punctuation for matching."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text


def extract_skills(text: str) -> Set[str]:
    """
    Extract skills using deterministic keyword matching.
    """
    text = normalize_text(text)
    found_skills = set()

    for skill in SKILL_LIST:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skill)

    return found_skills


def compute_skill_gap(resume_text: str, job_text: str) -> List[str]:
    """
    Identify skills present in job description but missing from resume.
    """
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    missing_skills = sorted(job_skills - resume_skills)
    return missing_skills
