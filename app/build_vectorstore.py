from ingestion.loaders import load_pdf, load_web, load_csv
from ingestion.chunking import chunk_documents
from retrieval.vectorstore import build_vectorstore

docs = []
docs.extend(load_pdf("../testing_scripts/sample.pdf"))
docs.extend(load_web("https://en.wikipedia.org/wiki/Retrieval-augmented_generation"))
docs.extend(load_csv("../testing_scripts/sample.csv"))

chunks = chunk_documents(docs)

print(f"Total chunks: {len(chunks)}")

build_vectorstore(chunks)
print("Vector store built and persisted.")
