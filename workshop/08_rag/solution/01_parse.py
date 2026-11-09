"""Step 1 – parse: PDFs in pdf/ -> text in markdown/. Run: uv run workshop/06_rag/solution/01_parse.py"""

from pathlib import Path

from pypdf import PdfReader

HERE = Path(__file__).parent
PDF_DIR = HERE / "pdf"
OUT_DIR = HERE / "markdown"
OUT_DIR.mkdir(exist_ok=True)

for pdf in sorted(PDF_DIR.glob("*.pdf")):
    reader = PdfReader(pdf)
    text = "\n\n".join(page.extract_text() for page in reader.pages)
    (OUT_DIR / f"{pdf.stem}.md").write_text(text, encoding="utf-8")
    print(f"{pdf.name}: {len(reader.pages)} pages -> markdown/{pdf.stem}.md")
