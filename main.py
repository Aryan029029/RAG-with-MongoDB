from src.loader import load_pdf
from src.cleaner import clean_pages
from src.chunking import chunk_documents

pages = load_pdf("data/pdfs/mongodb.pdf")

cleaned_pages = clean_pages(pages)

chunks = chunk_documents(cleaned_pages)

print(f"Original Pages : {len(pages)}")
print(f"Clean Pages    : {len(cleaned_pages)}")
print(f"Total Chunks   : {len(chunks)}")

print("\nExample Chunk:\n")

print(chunks[5].page_content)