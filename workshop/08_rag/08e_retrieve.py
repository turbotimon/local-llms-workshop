"""Step 4 – retrieve: top N chunks for a question. Run: uv run workshop/08_rag/08e_retrieve.py "your question" """

import sys
from pathlib import Path

import chromadb
import ollama

HERE = Path(__file__).parent
EMBED_MODEL = "nomic-embed-text"
N = 3

query = " ".join(sys.argv[1:]) or input("Question: ")

collection = chromadb.PersistentClient(path=HERE / "db").get_collection("docs")
query_embedding = ollama.embed(model=EMBED_MODEL, input=query).embeddings[0]
# IMPL: get the N most similar chunks (hint: collection.query(...))
result = {"ids": [[]], "documents": [[]], "distances": [[]]}

# result lists have one entry per query; we sent a single query
for id_, doc, dist in zip(result["ids"][0], result["documents"][0], result["distances"][0]):
    print(f"--- {id_} (distance {dist:.3f}) ---\n{doc}\n")
