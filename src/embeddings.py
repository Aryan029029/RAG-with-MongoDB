from sentence_transformers import SentenceTransformer

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text: str):
    """
    Generate embedding for a given text.
    """
    embedding = model.encode(text)
    return embedding.tolist()