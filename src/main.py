import ollama 
from vectore_store import add_chunks_to_store, search
from chunking import read_markdown_file, chunk_text

def generate_answer(question: str, context_chunks: list[str]) -> str :
    context = "\n\n".join(context_chunks)

    prompt = f"""Tu es un assistant pédagogique en cybersécurité. Réponds à la question en te basant UNIQUEMENT sur le contexte fourni ci-dessous. Si le contexte ne contient pas la réponse, dis-le clairement plutôt que d'inventer.

        Contexte : {context}
        Question : {question}
        Réponse :
    """

    reponse = ollama.chat(
        model = "mistral",
        messages=[{"role":"user", "content": prompt}]
    )
    return reponse["message", "content"]


if __name__ == "__main__":
    text = read_markdown_file("exemple_vault/cryptography_1.md")
    chunks = chunk_text(text)
    add_chunks_to_store(chunks, source_file="cryptography_1.md")
    print("Base de connaissances chargée.\n")

    while True:
        question = input("Pose ta question (ou 'quit' pour arrêter) : ")
        if question.lower() == "quit":
            break

        results = search(question)
        context_chunks = results["documents"][0]

        print("\nGénération de la réponse...\n")
        answer = generate_answer(question, context_chunks)
        print(f"Réponse : {answer}\n")
        print("-" * 50)
    