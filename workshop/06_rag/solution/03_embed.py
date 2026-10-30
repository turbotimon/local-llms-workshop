"""Step 3 – embed: chunks/ -> vectors in a Chroma db in db/. Run: uv run workshop/06_rag/solution/03_embed.py"""

from pathlib import Path

import chromadb
import ollama

HERE = Path(__file__).parent.parent
CHUNK_DIR = HERE / "chunks"
EMBED_MODEL = "nomic-embed-text"

files = sorted(CHUNK_DIR.glob("*.md"))
ids = [f.stem for f in files]
docs = [f.read_text(encoding="utf-8") for f in files]

# one request embeds all chunks: returns one vector per input text
embeddings = ollama.embed(model=EMBED_MODEL, input=docs).embeddings

client = chromadb.PersistentClient(path=HERE / "db")
collection = client.get_or_create_collection("docs")
collection.upsert(ids=ids, documents=docs, embeddings=embeddings)
print(f"Stored {collection.count()} chunks ({len(embeddings[0])} dimensions) in db/")
