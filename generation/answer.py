from generation.llm import get_llm
from langchain_core.prompts import ChatPromptTemplate

llm = get_llm()

confidence_prompt = ChatPromptTemplate.from_template("""
Answer the question using ONLY the context.

After the answer, rate your confidence as:
High / Medium / Low

Context:
{context}

Question:
{question}
""")

def generate_answer(question: str, context: str) -> str:
    response = llm.invoke(
        confidence_prompt.format(
            question=question,
            context=context
        )
    )
    return response.content
