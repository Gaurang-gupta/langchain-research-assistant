from retrieval.retriever import retrieve
from generation.baseline_rag import baseline_rag_answer

question = "What is retrieval augmented generation?"

docs = retrieve(question, k=4)

output = baseline_rag_answer(question, docs)

print("=== BASELINE RAG PROMPT ===")
print(output)
