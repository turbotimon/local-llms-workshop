"""Step 1 – parse: PDFs in pdf/ -> text in markdown/. Run: uv run workshop/08_rag/08b_parse.py"""

from pathlib import Path

from pypdf import PdfReader

HERE = Path(__file__).parent
PDF_DIR = HERE / "pdf"
OUT_DIR = HERE / "markdown"
OUT_DIR.mkdir(exist_ok=True)

for pdf in sorted(PDF_DIR.glob("*.pdf")):
    reader = PdfReader(pdf)
    # IMPL: extract the text of all pages and join them (hint: page.extract_text())
    text = ""
    (OUT_DIR / f"{pdf.stem}.md").write_text(text, encoding="utf-8")
    print(f"{pdf.name}: {len(reader.pages)} pages -> markdown/{pdf.stem}.md")
