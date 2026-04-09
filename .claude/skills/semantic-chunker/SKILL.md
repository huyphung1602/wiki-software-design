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

After Pass 1 completes, perform AI-guided chapter boundary detection:

1. **Read TOC**: Read first 500 lines of `raw/<book-name>/<book-name>.txt` to find all chapter headings and their numbers. Build a list of chapter titles.

2. **Read all Pass 1 chunks**: List all `raw/<book-name>/chunks/chunk-*.md` files. For each chunk, read:
   - First 200 words
   - Last 200 words
   - Any `[Image: ...]` placeholders (to track which images belong to which chunk)

3. **Detect chapter boundaries**: For each Pass 1 chunk, determine:
   - Which chapter(s) the content belongs to
   - Whether it overlaps chapter boundaries (a chunk spanning two chapters must be split)
   - The chapter title from the TOC

4. **CRITICAL constraint: One chunk must NOT span multiple chapters.** If a Pass 1 chunk contains content from two different chapters, split it into two separate chunks at the chapter boundary.

5. **Rewrite chunks**: Create new chunk files that are aligned to chapter boundaries:
   - Each chunk belongs to exactly ONE chapter
   - A chapter may produce multiple chunks (use `(cont.)` suffix in map.md for continuation)
   - The chunk starts with the chapter heading or continues from where the previous chunk ended

6. **Write map.md**: Create `raw/<book-name>/map.md` with the chapter mapping and image index

7. **Collect image information**: For each chunk, record which images appear in it (from `[Image: ...]` placeholders) so wiki-ingest knows where to place them.

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

| Chunk | Chapter | Title | Images |
|-------|---------|-------|--------|
| chunk-001 | 1 | Introduction | |
| chunk-002 | 2 | Complexity | |
| chunk-003 | 2 | Complexity (cont.) | `page-026-fig-01.png` |
| chunk-004 | 3 | Approaches | `page-033-fig-01.png`, `page-035-fig-01.png` |

## Image Index

| Image | Chapter | Description |
|-------|---------|-------------|
| `page-026-fig-01.png` | Ch 2 | Table classifying data types |
| `page-033-fig-01.png` | Ch 3 | Comparison of approaches |
```

Rules:
- A chapter may span multiple chunks (marked with "(cont.)")
- One chunk must NOT span multiple chapters
- The Images column lists `[Image: ...]` placeholders found in that chunk
- The Image Index section at bottom helps wiki-ingest understand image placement

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
