from src.loader import load_pdf

pages = load_pdf("data/pdfs/mongodb.pdf")

print(f"Total Pages: {len(pages)}")

print("\nFirst Page:\n")

print(pages[0].page_content)