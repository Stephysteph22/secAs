import chromadb
from chunking import read_markdown_file, chunk_text
from embeddings import embed_chunks

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(name="cours")

def add_chunks_to_store(chunks: list[str], source_file: str):
    embeddings = embed_chunks(chunks)
    ids = [f"{source_file}_chunk_{i}" for i in range(len(chunks))]
    metadatas = [{"source": source_file} for _ in chunks]

    collection.add(
        ids=ids,
        embeddings=embeddings.tolist(), #en liste car les tableau numpy ne sont pas pris accepté par chroma
        documents=chunks,
        metadatas=metadatas
    )


def search(query: str, n_results: int = 3):
    query_embedding = embed_chunks([query])[0]

    results = collection.query(
        query_embeddings= [query_embedding.tolist()], 
            n_results=n_results
    )
    return results


if __name__ == "__main__" :
    text = read_markdown_file("exemple_vault/cryptography_1.md")
    chunks = chunk_text(text)

    add_chunks_to_store(chunks, source_file="cryptography_1.md" )
    print(f"{len(chunks)} chunks ajoutés à la base vectorielle.")

    question = input("\n Pose moi une question...")
    results = search(question)

    print(f"\nQuestion : {question}")
    print("\nChunks les plus pertinents trouvés :")
    for doc, distance in zip(results["documents"][0], results["distances"][0]):
        print(f"\n(distance: {distance:.4f})")
        print(doc[:200], "...")


