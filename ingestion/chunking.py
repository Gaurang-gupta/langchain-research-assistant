from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document

def chunk_documents(
    documents: List[Document],
    chunk_size: int = 800,
    chunk_overlap: int = 150
) -> List[Document]:
    """
    Chunk documents using a recursive strategy to preserve semantic coherence.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = splitter.split_documents(documents)

    for idx, chunk in enumerate(chunks):
        chunk.metadata.update({
            "chunk_id": idx
        })

    return chunks
