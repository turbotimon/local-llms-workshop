# 06 – Local RAG

Pipeline: `pdf/` → parse → `markdown/` → chunk → `chunks/` → embed → `db/` → retrieve → generate

## Setup

```sh
ollama pull nomic-embed-text
ollama pull gemma4:e4b
```

Put your PDF(s) into `pdf/`.

## Run each step in order

```sh
uv run workshop/06_rag/01_parse.py
uv run workshop/06_rag/02_chunk.py
uv run workshop/06_rag/03_embed.py
uv run workshop/06_rag/04_retrieve.py "your question"
uv run workshop/06_rag/05_generate.py "your question"
```

IMPL: fill in the `# IMPL:` lines in every file. Look at the output folder after each step.
Stuck? See `solution/`.

Try: change `CHUNK_SIZE`, `STRATEGY` or `N` and compare the answers.
