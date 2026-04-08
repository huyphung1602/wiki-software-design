---
name: pdf-extractor
description: Extract text from a PDF into a single txt file in raw/. Use when user invokes /pdf-extractor or wants to process a PDF into the wiki pipeline.
allowed-tools: Bash,Read,Write
---

# PDF Extractor Skill

## Role

**Extract text and images from PDF → txt file + image files in raw/**

Called via `/pdf-extractor` slash command or by the orchestrator when chaining skills.

**Position in flow**: `PDF → pdf-extractor → raw/<book-name>/<book-name>.txt + raw/<book-name>/images/`

## How to Use This Skill

When invoked via Skill tool:

```bash
python3 .claude/skills/pdf-extractor/pdf_extractor.py "<pdf-path>" "raw/<book-name>/<book-name>.txt"
```

Where `<book-name>` is derived from the PDF filename: lowercase, spaces → hyphens, strip extension.
Example: `Design Patterns.pdf` → `design-patterns`

Steps:
1. Derive book name from PDF filename
2. Create directory: `raw/<book-name>/`
3. Run the extraction script with output path in `raw/`

## Input/Output

**Input**: Path to PDF file
**Output**: `raw/<book-name>/<book-name>.txt` — full extracted text with page separators and `[Image: ...]` placeholders
**Additional output**: `raw/<book-name>/images/page-NNN-img-MM.<ext>` — extracted images from the PDF

## Dependencies

```bash
pip install pdfplumber pymupdf
```

## What NOT to Do

❌ DO NOT manually extract text
❌ DO NOT use pdftotext
❌ DO NOT output JSON
❌ DO NOT modify files in raw/ after creation (exception: pdf-extractor may overwrite during re-extraction)

✅ DO run the pdf_extractor.py script
✅ DO write output to raw/<book-name>/

## Script Location

```
.claude/skills/pdf-extractor/
├── SKILL.md
└── pdf_extractor.py
```

## Example

```bash
python3 .claude/skills/pdf-extractor/pdf_extractor.py "Design Patterns.pdf" "raw/design-patterns/design-patterns.txt"
```

## Image Extraction

The script also extracts embedded images from each PDF page:
- Images are saved to `raw/<book-name>/images/` directory
- `[Image: page-NNN-img-MM.ext]` placeholders appear in the text at approximate image positions
- Vector graphics (common in technical diagrams) are rendered as PNG
- If no images are found in the PDF, the output is identical to the old behavior
