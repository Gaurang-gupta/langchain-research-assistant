from typing import List
from langchain_core.documents import Document
from generation.prompt import BASELINE_RAG_PROMPT
from langchain_google_genai import ChatGoogleGenerativeAI

def format_context(documents: List[Document]) -> str:
    formatted = []
    for doc in documents:
        source = doc.metadata.get("source", "unknown")
        formatted.append(
            f"[source: {source}]\n{doc.page_content}"
        )
    return "\n\n".join(formatted)


def baseline_rag_answer(question: str, documents: List[Document]) -> str:
    """
    Baseline RAG without agents or tools.
    """

    context = format_context(documents)

    # prompt = BASELINE_RAG_PROMPT.format(
    #     context=context,
    #     question=question
    # )

    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3
    )

    chain = BASELINE_RAG_PROMPT | model

    # TEMPORARY: no LLM call yet
    # We return the prompt to inspect grounding quality
    result = chain.invoke({
        "context": context,
        "question": question,
    })
    return result.content
