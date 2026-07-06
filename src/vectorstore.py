import faiss
import pickle
import numpy as np

index = faiss.IndexFlatL2(384)

documents = []


def save():

    faiss.write_index(index, "faiss.index")

    with open("documents.pkl", "wb") as f:
        pickle.dump(documents, f)


def load():

    global index
    global documents

    try:

        index = faiss.read_index("faiss.index")

        with open("documents.pkl", "rb") as f:
            documents = pickle.load(f)

    except:

        pass