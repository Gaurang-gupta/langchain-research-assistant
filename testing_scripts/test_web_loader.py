from ingestion.loaders import load_web

URL = "https://en.wikipedia.org/wiki/Retrieval-augmented_generation"

docs = load_web(URL)

print(f"Loaded {len(docs)} web documents")

doc = docs[0]
print("Content preview:")
print(doc.page_content)

print("Metadata:")
print(doc.metadata)
