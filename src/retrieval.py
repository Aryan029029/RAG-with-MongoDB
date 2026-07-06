import numpy as np
from sentence_transformers import SentenceTransformer

from src.vectorstore import index, documents, load

load()

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def retrieve(query, k=3):

    embedding = model.encode(query).astype(np.float32)

    distances, indices = index.search(np.array([embedding]), k)

    results = []

    for idx in indices[0]:

        if idx != -1:

            results.append(documents[idx])

    return results