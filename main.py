from src.loader import load_pdf
from src.cleaner import clean_pages

pages = load_pdf("data/pdfs/mongodb.pdf")

print(f"Pages before cleaning : {len(pages)}")

cleaned_pages = clean_pages(pages)

print(f"Pages after cleaning  : {len(cleaned_pages)}")