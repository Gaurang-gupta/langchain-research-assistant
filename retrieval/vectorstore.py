import os
from typing import List
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from retrieval.embeddings import get_embeddings
from config.settings import settings


def build_vectorstore(documents: List[Document]) -> FAISS:
    embeddings = get_embeddings()

    vectorstore = FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )

    os.makedirs(settings.vectorstore_path, exist_ok=True)
    vectorstore.save_local(settings.vectorstore_path)

    return vectorstore


def load_vectorstore() -> FAISS:
    embeddings = get_embeddings()
    return FAISS.load_local(
        settings.vectorstore_path,
        embeddings,
        allow_dangerous_deserialization=True
    )
