from ingestion.loaders import load_csv

PATH = "sample.csv"

docs = load_csv(PATH)

print(f"Loaded {len(docs)} CSV documents")

doc = docs[0]
print("Content:")
print(doc.page_content)

print("Metadata:")
print(doc.metadata)
