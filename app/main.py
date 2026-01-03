from retrieval.retriever import retrieve, bm25_retrieve, deduplicate_docs
from retrieval.context_compressor import compress_documents
from generation.answer import generate_answer
from routing.query_classifier import classify_query


def run_rag(question: str):
    intent = classify_query(question)

    if intent != "factual":
        return {
            "answer": "I can only answer factual questions based on the provided documents.",
            "documents": []
        }

    initial_docs = retrieve(question)
    bm25_docs = bm25_retrieve(initial_docs, question)

    docs = deduplicate_docs(initial_docs + bm25_docs)
    compressed_docs = compress_documents(docs)

    answer = generate_answer(question, compressed_docs)

    if "Low" in answer:
        return {
            "answer": "I don't have enough information to answer confidently.",
            "documents": []
        }

    return {
        "answer": answer,
        "documents": compressed_docs
    }

if "__main__" == __name__:
    run_rag("What is Retrieval Augmented Generation?")