---
name: pdf-extractor
description: Extract text from a PDF into a single txt file in raw/. Use when user invokes /pdf-extractor or wants to process a PDF into the wiki pipeline.
allowed-tools: Bash,Read,Write
---

# PDF Extractor Skill

## Role

**Extract text from PDF → single txt file in raw/**

Called via `/pdf-extractor` slash command or by the orchestrator when chaining skills.

**Position in flow**: `PDF → pdf-extractor → raw/<book-name>/<book-name>.txt`

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
**Output**: `raw/<book-name>/<book-name>.txt` — full extracted text with page separators

## Dependencies

```bash
pip install pdfplumber
```

## What NOT to Do

❌ DO NOT manually extract text
❌ DO NOT use pdftotext
❌ DO NOT output JSON
❌ DO NOT modify files in raw/ after creation

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
