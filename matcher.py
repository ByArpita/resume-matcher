# matcher.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load model once at import time (efficient & deterministic)
MODEL_NAME = "all-MiniLM-L6-v2"
model = SentenceTransformer(MODEL_NAME)


def compute_match_score(resume_text: str, job_text: str) -> float:
    """
    Compute cosine similarity between resume and job description.
    Returns a percentage score between 0 and 100.
    """

    # Encode texts into fixed embeddings
    embeddings = model.encode(
        [resume_text, job_text],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    resume_vec, job_vec = embeddings

    # Cosine similarity
    similarity = cosine_similarity(
        resume_vec.reshape(1, -1),
        job_vec.reshape(1, -1)
    )[0][0]

    # Scale to percentage
    score = round(similarity * 100, 2)
    return score
