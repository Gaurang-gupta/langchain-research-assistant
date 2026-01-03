from ingestion.loaders import load_pdf
from ingestion.chunking import chunk_documents
from dotenv import load_dotenv
load_dotenv()
import os

if not os.getenv("USER_AGENT"):
    os.environ["USER_AGENT"] = "LangChainResearchAssistant/1.0"
docs = load_pdf("sample.pdf")
chunks = chunk_documents(docs)

print(f"Loaded {len(docs)} documents")
print(f"Generated {len(chunks)} chunks")
print(chunks[0].metadata)
