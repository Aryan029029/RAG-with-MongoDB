from src.loader import load_pdf
from src.cleaner import clean_pages
from src.chunking import chunk_documents
from src.embeddings import get_embedding
from src.database import collection


def ingest():

    pages = load_pdf("data/pdfs/mongodb.pdf")

    cleaned_pages = clean_pages(pages)

    chunks = chunk_documents(cleaned_pages)

    collection.delete_many({})

    documents = []

    for chunk in chunks:

        documents.append(
            {
                "text": chunk.page_content,
                "embedding": get_embedding(chunk.page_content),
                "metadata": chunk.metadata,
            }
        )

    collection.insert_many(documents)

    print(f"Inserted {len(documents)} documents into MongoDB.")