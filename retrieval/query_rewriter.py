from langchain_core.prompts import PromptTemplate
from generation.llm import get_llm

llm = get_llm()

rewrite_prompt = PromptTemplate.from_template("""
Rewrite the user query into 3 diverse, search-optimized queries.

Query: {question}

Return each query on a new line.
""")

def rewrite_query(question: str) -> list[str]:
    response = llm.invoke(
        rewrite_prompt.format(question=question)
    )
    return [q.strip() for q in response.content.split("\n") if q.strip()]
