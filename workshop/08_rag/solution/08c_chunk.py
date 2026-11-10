"""Step 2 – chunk: markdown/ -> small text pieces in chunks/. Run: uv run workshop/08_rag/08c_chunk.py"""

import re
from pathlib import Path

HERE = Path(__file__).parent
IN_DIR = HERE / "markdown"
OUT_DIR = HERE / "chunks"
OUT_DIR.mkdir(exist_ok=True)

CHUNK_SIZE = 1000  # characters per chunk


def chunk(text):
    # 1. slice at empty lines (paragraphs)
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]

    # 2. pack paragraphs into chunks up to CHUNK_SIZE characters;
    #    paragraphs longer than CHUNK_SIZE are cut into pieces of CHUNK_SIZE
    chunks, current = [], ""
    for para in paragraphs:
        for i in range(0, len(para), CHUNK_SIZE):
            piece = para[i : i + CHUNK_SIZE]
            if current and len(current) + 2 + len(piece) > CHUNK_SIZE:
                chunks.append(current)
                current = piece
            else:
                current = f"{current}\n\n{piece}" if current else piece
    if current:
        chunks.append(current)
    return chunks


for md in sorted(IN_DIR.glob("*.md")):
    chunks = chunk(md.read_text(encoding="utf-8"))
    for i, c in enumerate(chunks):
        (OUT_DIR / f"{md.stem}_{i}.md").write_text(c, encoding="utf-8")
    print(f"{md.name}: {len(chunks)} chunks")