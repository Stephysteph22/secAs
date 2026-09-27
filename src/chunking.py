from pathlib import Path

def read_markdown_file(filepath: str) -> str:       #Lit un fichier markdown et retourne son contenu brut
    return Path(filepath).read_text(encoding="utf-8")   

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:      #Découpe un texte en chunks de chunks_size mots, avec un chevauchement de 'overlap' mots entre chaque chunk 
    words = text.split()
    chunks = []
    start = 0  

    while start < len(words):        
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap 
    return chunks 

if __name__ == "__main__": 
    text = read_markdown_file("exemple_vault/cryptography_1.md")
    chunks = chunk_text(text)

    print(f"Nombre de chunks crées : {len(chunks)}")
    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i} ---")
        print(chunk[:200], "...")  #Affiche que le début pour ne pas spammer