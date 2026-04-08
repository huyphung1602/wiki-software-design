# Software Design Wiki

A personal knowledge base on software design, powered by [Quartz v4](https://quartz.jzhao.xyz/).

## Content Structure

- `raw/` — Immutable source PDFs (processed by pdf-extractor)
- `content/` — LLM-authored markdown pages (books, concepts, comparisons)
- `.claude/skills/` — LLM tools for content workflows

## LLM Skills

| Skill | Purpose |
|-------|---------|
| `/pdf-extractor <file>` | Extract text from a PDF into `raw/` |
| `/semantic-chunker <book>` | Split extracted text into chapter-aligned chunks |
| `/wiki-ingest <book> [N]` | Ingest a chunk into content pages |
| `/wiki-query <question>` | Search content and synthesize answers |
| `/wiki-lint` | Check for orphans, broken links, contradictions |
| `/wiki-compare [a] [b]` | Create comparison pages between concepts |

### Skill Workflows

**Ingest a book:**
1. `/pdf-extractor <book.pdf>` — extract PDF to `raw/`
2. `/semantic-chunker <book>` — chunk the text
3. `/wiki-ingest <book>` — process chunks into content (repeat for each chunk)
4. `/wiki-lint` — verify quality
5. `npx quartz sync --no-pull` — commit and push to GitHub

**Query the knowledge base:**
1. `/wiki-query <question>` — get synthesized answer
2. Optionally file the answer as a new page

## Deploying with Quartz

This repo uses Quartz v4 to publish content as a static site.

**Sync and deploy:**
```bash
npx quartz sync --no-pull
```

Flags:
- `--no-pull` — don't merge from upstream (use when content conflicts)
- `-v` — verbose logging
- `--commit` / `--no-push` — control git behavior

**Full workflow:**
```bash
# After ingesting content
npx quartz sync --no-pull
```

See [Quartz docs](https://quartz.jzhao.xyz/setting-up-your-GitHub-repository) for details.
