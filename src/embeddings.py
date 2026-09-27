from sentence_transformers import SentenceTransformer
from chunking import read_markdown_file, chunk_text

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks: list[str]):
    embeddings = model.encode(chunks)
    return embeddings 

if __name__ == "__main__": 
    text = read_markdown_file("exemple_vault/cryptography_1.md")
    chunks = chunk_text(text)

    embeddings = embed_chunks(chunks)

    print(f"Nombre de chunks : {len(chunks)}")
    print(f"Dimension de chaque vecteur : {embeddings[0].shape}")
    print(f"\nAperçu du 1er vecteur (10 premières valeurs) :")
    print(embeddings[0][:10])