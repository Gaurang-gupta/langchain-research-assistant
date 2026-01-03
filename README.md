# LangChain Research Assistant

A modular **Retrieval-Augmented Generation (RAG)** system built with LangChain that answers factual questions by retrieving relevant context from documents and generating grounded responses.

This project focuses on **core RAG architecture and correctness**, not UI or deployment polish.

---

## Why This Project Exists

Most “AI assistants” demos jump straight to APIs and UIs while hiding weak fundamentals.

This project intentionally stops at a **fully working RAG pipeline**:
- Document ingestion
- Vector indexing
- Retrieval + compression
- Answer generation with sources

This makes it suitable for **technical evaluation, learning, and extension**.

---

## What It Does

- Ingests structured and unstructured documents (PDF, CSV, text)
- Converts documents into embeddings
- Stores embeddings in a FAISS vector store
- Retrieves relevant chunks for a user query
- Generates answers grounded in retrieved context
- Returns both the **answer and source documents**

---

## What It Does NOT Do (By Design)

- No frontend UI
- No hosted API deployment
- No authentication or billing
- No “chatbot” gimmicks

Those can be added later, but they are intentionally excluded here.

---

## Project Structure
```bash
├── app/
│ ├── api.py # FastAPI endpoint (optional, not required to run core logic)
│ ├── pipeline.py # Core RAG pipeline (retrieval + generation)
│ ├── schemas.py # Pydantic request/response models
│ ├── loaders.py # Document loaders (PDF, CSV, web)
│ ├── vectorstore.py # FAISS index creation and loading
│ └── ui.py # Placeholder (not wired intentionally)
│
├── data/
│ └── documents/ # Source documents
│
├── main.py # Entry point for local testing
├── requirements.txt
└── README.md
```


---

## Core Pipeline Flow

1. Load documents from disk
2. Chunk documents
3. Generate embeddings
4. Store embeddings in FAISS
5. Retrieve top-k relevant chunks for a query
6. Compress context to reduce noise
7. Generate final answer using retrieved context

---

## Tech Stack

- Python 3.x
- LangChain
- FAISS (vector search)
- Hugging Face sentence-transformer embeddings
- FastAPI (optional API layer)
- Pydantic

---

## Running Locally (No API)

```bash
pip install -r requirements.txt
python main.py
```

## Optional: API Layer

A FastAPI endpoint exists in app/api.py for experimentation, but the project is considered complete without it.
This separation keeps the core RAG logic reusable across:

1. APIs
2. CLIs
3. Background jobs
4. Future UIs

## Design Decisions
1. Separation of concerns: retrieval, generation, schemas, and IO are isolated
2. Explicit pipeline instead of agent magic
3. Testable without a server
4. Resume-friendly: shows real system design, not wrappers

## Possible Extensions

1. Add frontend (Next.js / Streamlit)
2. Add streaming responses
3. Add hybrid search (BM25 + vector)
4. Add evaluation metrics
5. Swap LLM providers
