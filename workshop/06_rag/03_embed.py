"""Step 3 – embed: chunks/ -> vectors in a Chroma db in db/. Run: uv run workshop/06_rag/03_embed.py"""

from pathlib import Path

import chromadb
import ollama

HERE = Path(__file__).parent
CHUNK_DIR = HERE / "chunks"
EMBED_MODEL = "nomic-embed-text"

files = sorted(CHUNK_DIR.glob("*.md"))
ids = [f.stem for f in files]
docs = [f.read_text(encoding="utf-8") for f in files]

# IMPL: embed all chunks with Ollama -> one vector per chunk (hint: ollama.embed(...).embeddings)
embeddings = []

client = chromadb.PersistentClient(path=HERE / "db")
collection = client.get_or_create_collection("docs")
collection.upsert(ids=ids, documents=docs, embeddings=embeddings)
print(f"Stored {collection.count()} chunks ({len(embeddings[0])} dimensions) in db/")
