# 08 – Local RAG

Pipeline: `pdf/` → parse → `markdown/` → chunk → `chunks/` → embed → `db/` → retrieve → generate

## Setup

```sh
ollama pull nomic-embed-text
ollama pull gemma4:e4b
```

Put your PDF(s) into `pdf/`.

## Run each step in order

```sh
uv run workshop/08_rag/08b_parse.py
uv run workshop/08_rag/08c_chunk.py
uv run workshop/08_rag/08d_embed.py
uv run workshop/08_rag/08f_retrieve.py "your question"
uv run workshop/08_rag/08e_generate.py "your question"
```

IMPL: fill in the `# IMPL:` lines in every file. Look at the output folder after each step.
Stuck? See `solution/`.

Try: change `CHUNK_SIZE`, `STRATEGY` or `N` and compare the answers.
