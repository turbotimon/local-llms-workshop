"""Step 5 – generate: answer a question with retrieved context. Run: uv run workshop/06_rag/05_generate.py "your question" """

import sys
from pathlib import Path

import chromadb
import ollama

HERE = Path(__file__).parent
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "gemma4:e4b"
N = 3

query = " ".join(sys.argv[1:]) or input("Question: ")

# retrieve (same as 04_retrieve.py)
collection = chromadb.PersistentClient(path=HERE / "db").get_collection("docs")
query_embedding = ollama.embed(model=EMBED_MODEL, input=query).embeddings[0]
docs = collection.query(query_embeddings=[query_embedding], n_results=N)["documents"][0]

context = "\n\n---\n\n".join(docs)
# IMPL: build a prompt that tells the LLM to answer the query using only the context
prompt = query

response = ollama.chat(model=CHAT_MODEL, messages=[{"role": "user", "content": prompt}])
print(response.message.content)
