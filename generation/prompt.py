from langchain_core.prompts import ChatPromptTemplate
BASELINE_RAG_PROMPT = ChatPromptTemplate.from_template("""
You are an assistant answering questions strictly using the provided context.

Rules:
- Use ONLY the context.
- If the answer is not present, say "I don't know".
- Do not add external knowledge.
- Cite sources using [source].

Context:
{context}

Question:
{question}

Answer:
"""
)