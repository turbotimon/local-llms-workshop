"""Step 5 – generate: answer a question with retrieved context. Run: uv run workshop/06_rag/solution/05_generate.py "your question" """

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

# augment: put the retrieved chunks into the prompt
context = "\n\n---\n\n".join(docs)
prompt = (
    "Answer the question using only the context below. "
    "If the answer is not in the context, say so.\n\n"
    f"Context:\n{context}\n\nQuestion: {query}"
)

response = ollama.chat(model=CHAT_MODEL, messages=[{"role": "user", "content": prompt}])
print(response.message.content)
