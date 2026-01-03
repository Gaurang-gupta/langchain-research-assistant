from generation.llm import get_llm
from langchain_core.prompts import PromptTemplate

llm = get_llm()

compress_prompt = PromptTemplate.from_template("""
Summarize the following content into concise factual points.
Remove redundancy. Preserve technical accuracy.

Content:
{context}
""")

def compress_documents(docs):
    combined_text = "\n\n".join(doc.page_content for doc in docs)

    response = llm.invoke(
        compress_prompt.format(context=combined_text)
    )

    return response.content
