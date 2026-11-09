"""Step 2 – chunk: markdown/ -> small text pieces in chunks/. Run: uv run workshop/06_rag/solution/02_chunk.py"""

import re
from pathlib import Path

HERE = Path(__file__).parent
IN_DIR = HERE / "markdown"
OUT_DIR = HERE / "chunks"
OUT_DIR.mkdir(exist_ok=True)

STRATEGY = "length"  # "length" or "header"
CHUNK_SIZE = 600  # characters per chunk
HEADER_LEVEL = 2  # split at "## " headers (and higher levels)


def chunk_by_length(text):
    return [text[i : i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]


def chunk_by_header(text):
    # split before every line starting with 1..HEADER_LEVEL "#"
    parts = re.split(rf"(?m)^(?=#{{1,{HEADER_LEVEL}}} )", text)
    chunks = [p for p in parts if p.strip()]
    # fall back to length if there are no headers (e.g. plain pypdf text)
    return chunks if len(chunks) > 1 else chunk_by_length(text)


for md in sorted(IN_DIR.glob("*.md")):
    text = md.read_text(encoding="utf-8")
    chunks = chunk_by_header(text) if STRATEGY == "header" else chunk_by_length(text)
    for i, chunk in enumerate(chunks):
        (OUT_DIR / f"{md.stem}_{i}.md").write_text(chunk, encoding="utf-8")
    print(f"{md.name}: {len(chunks)} chunks")
