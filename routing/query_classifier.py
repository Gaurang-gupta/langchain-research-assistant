from generation.llm import get_llm
from langchain_core.prompts import PromptTemplate

llm = get_llm()

intent_prompt = PromptTemplate.from_template("""
Classify the query into one of:
- factual
- conversational
- ambiguous
- out_of_scope

Query: {query}

Return only the label.
""")

def classify_query(query: str) -> str:
    response = llm.invoke(intent_prompt.format(query=query))
    return response.content.strip().lower()
