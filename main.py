from src.ingest import ingest
from src.retrieval import retrieve

print("Building vector database...")

ingest()

print("Ready!\n")

while True:

    query = input("Question: ")

    if query.lower() == "exit":
        break

    docs = retrieve(query)

    print("\nTop Results\n")

    for i, doc in enumerate(docs, start=1):

        print("=" * 80)
        print(f"Result {i}")
        print("=" * 80)
        print(doc.page_content)
        print()