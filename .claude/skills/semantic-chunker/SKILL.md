---
name: semantic-chunker
description: Split extracted book text into semantic chunks aligned to chapter boundaries. Use after pdf-extractor or when user invokes /semantic-chunker. Two-pass: script chunking then AI chapter detection.
allowed-tools: Bash,Read,Write,Glob,Grep
---

# Semantic Chunker Skill

## Role

**Sliding window chunking + AI chapter detection**

Two-pass process:
- Pass 1 (script): Mechanical sliding window → rough chunks
- Pass 2 (LLM): Read overlapping windows, detect chapter breaks → clean chunks + map.md

**Position in flow**: `raw/<book>/<book>.txt → semantic-chunker → raw/<book>/chunks/*.md + map.md`

## Pass 1: Script Chunking (NO AI)

Run the chunking script:

```bash
python3 .claude/skills/semantic-chunker/chunker.py "raw/<book-name>/<book-name>.txt" "raw/<book-name>/chunks" [--window 5000] [--overlap 500]
```

Defaults: window=5000 words, overlap=500 words.

## Pass 2: AI Chapter Detection (YES AI)

After Pass 1 completes:

1. **Read TOC hints**: Read first 500 lines of `raw/<book-name>/<book-name>.txt` to find chapter headings, table of contents
2. **Sample chunks**: For each chunk from Pass 1, read first 200 + last 200 words
3. **Detect boundaries**: Identify where actual chapter/section breaks fall within the overlapping chunks
4. **Rewrite chunks**: Overwrite Pass 1 chunk files with clean chunks aligned to real chapter boundaries
5. **Write map.md**: Create `raw/<book-name>/map.md` linking chunks to chapters

## Chunk File Format

Each chunk is plain markdown:
```markdown
# Chapter 1: Introduction

<extracted text content>
```

No YAML frontmatter. Chunks are raw source material.

## map.md Format

```markdown
# Chunk Map: <book-name>

| Chunk | Chapter | Title |
|-------|---------|-------|
| chunk-001 | 1 | Introduction |
| chunk-002 | 2 | Creational Patterns |
| chunk-003 | 2 | Creational Patterns (cont.) |
```

A chapter may span multiple chunks (marked with "cont.").

## What NOT to Do

❌ DO NOT manually split chunks
❌ DO NOT skip Pass 2 — Pass 1 chunks are rough, not final
❌ DO NOT modify chunks or map.md after this skill completes (they are immutable for wiki-ingest)

✅ DO run the chunking script for Pass 1
✅ DO perform AI chapter detection for Pass 2
✅ DO overwrite Pass 1 chunks with final aligned chunks

## Script Location

```
.claude/skills/semantic-chunker/
├── SKILL.md
└── chunker.py
```
