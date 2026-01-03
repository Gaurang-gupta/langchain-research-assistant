from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import (
    PyPDFLoader,
    WebBaseLoader,
    CSVLoader
)
from typing import List
from langchain_core.documents import Document
import os

print("USER_AGENT =", os.getenv("USER_AGENT"))

def load_pdf(path: str) -> List[Document]:
    loader = PyPDFLoader(path)
    docs = loader.load()
    for d in docs:
        d.metadata.update({
            "source_type": "pdf",
            "source": path
        })
    return docs


def load_web(url: str) -> List[Document]:
    loader = WebBaseLoader(url)
    docs = loader.load()
    for d in docs:
        d.metadata.update({
            "source_type": "web",
            "source": url
        })
    return docs


def load_csv(path: str) -> List[Document]:
    loader = CSVLoader(file_path=path)
    docs = loader.load()
    for d in docs:
        d.metadata.update({
            "source_type": "csv",
            "source": path
        })
    return docs
