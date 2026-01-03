from retrieval.vectorstore import load_vectorstore
from retrieval.query_rewriter import rewrite_query
from rank_bm25 import BM25Okapi

def bm25_retrieve(docs, query, k=4):
    corpus = [d.page_content for d in docs]
    tokenized = [c.split() for c in corpus]

    bm25 = BM25Okapi(tokenized)
    scores = bm25.get_scores(query.split())

    ranked = sorted(
        zip(docs, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [doc for doc, _ in ranked[:k]]

def deduplicate_docs(docs):
    seen = set()
    unique_docs = []

    for doc in docs:
        if doc.page_content not in seen:
            unique_docs.append(doc)
            seen.add(doc.page_content)

    return unique_docs

def retrieve(question: str, k: int = 4):
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": k}
    )

    rewritten_queries = rewrite_query(question)

    all_docs = []
    for q in rewritten_queries:
        docs = retriever.invoke(q)
        all_docs.extend(docs)

    return deduplicate_docs(all_docs)
