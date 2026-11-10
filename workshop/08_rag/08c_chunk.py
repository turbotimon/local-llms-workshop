"""Step 2 – chunk: markdown/ -> small text pieces in chunks/. Run: uv run workshop/08_rag/08c_chunk.py"""

import re
from pathlib import Path

HERE = Path(__file__).parent
IN_DIR = HERE / "markdown"
OUT_DIR = HERE / "chunks"
OUT_DIR.mkdir(exist_ok=True)

CHUNK_SIZE = 1000  # characters per chunk

def chunk(text):
    # IMPL 1. slice at empty lines (paragraphs)
    paragraphs = ...

    # IMPL 2. pack paragraphs into chunks up to CHUNK_SIZE characters;
    #    paragraphs longer than CHUNK_SIZE are cut into pieces of CHUNK_SIZE
    chunks = ...

    return chunks


for md in sorted(IN_DIR.glob("*.md")):
    chunks = chunk(md.read_text(encoding="utf-8"))
    for i, c in enumerate(chunks):
        (OUT_DIR / f"{md.stem}_{i}.md").write_text(c, encoding="utf-8")
    print(f"{md.name}: {len(chunks)} chunks")
