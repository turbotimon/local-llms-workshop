"""Step 1 – parse (PyMuPDF): PDFs in pdf/ -> text in markdown/. Run: uv run --with pymupdf workshop/08_rag/08b_parse_pymupdf.py"""

from pathlib import Path

import pymupdf

HERE = Path(__file__).parent
PDF_DIR = HERE / "pdf"
OUT_DIR = HERE / "markdown"
OUT_DIR.mkdir(exist_ok=True)

for pdf in sorted(PDF_DIR.glob("*.pdf")):
    with pymupdf.open(pdf) as doc:
        # extract the text of all pages and join them (hint: page.get_text())
        text = "\n".join(page.get_text() for page in doc)
        n_pages = doc.page_count
    (OUT_DIR / f"{pdf.stem}.md").write_text(text, encoding="utf-8")
    print(f"{pdf.name}: {n_pages} pages -> markdown/{pdf.stem}.md")
