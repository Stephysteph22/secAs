import chromadb
from chunking import read_markdown_file, chunk_text
from embeddings import embed_chunks

client = chromadb.PersistentClient(path="chroma_db")

def get_collection(name: str = "cours"):
    return client.get_or_create_collection(name=name)

def reset_collection(name: str):
    try:
        client.delete_collection(name)
    except Exception:
        pass  # la collection n'existe pas encore

def add_chunks_to_store(chunks, source_file, collection_name="cours"):
    collection = get_collection(collection_name)
    embeddings = embed_chunks(chunks)
    ids = [f"{source_file}_chunk_{i}" for i in range(len(chunks))]
    metadatas = [{"source": source_file} for _ in chunks]
    collection.upsert(
        ids=ids,
        embeddings=embeddings.tolist(),
        documents=chunks,
        metadatas=metadatas,
    )

def search(query, n_results=3, collection_name="cours"):
    collection = get_collection(collection_name)
    query_embedding = embed_chunks([query])[0]
    return collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results,
    )

