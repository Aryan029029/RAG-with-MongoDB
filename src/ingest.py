from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np

from src.vectorstore import index, documents, save

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def ingest():

    loader = PyPDFLoader("data/pdfs/mongodb.pdf")
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=150
    )

    docs = splitter.split_documents(pages)

    index.reset()
    documents.clear()

    for doc in docs:

        embedding = model.encode(doc.page_content).astype(np.float32)

        index.add(np.array([embedding]))

        documents.append(doc)

    save()

    print(f"Ingested {len(documents)} chunks.")