from app.pipeline import run_rag

if __name__ == "__main__":
    q = "Explain quantum teleportation in ants"
    result = run_rag(q)

    print("ANSWER:")
    print(result["answer"])
    print("\nDOCUMENTS USED:", len(result["documents"]))
