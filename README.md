# Software Design Wiki

A personal knowledge base on software design, powered by [Quartz v4](https://quartz.jzhao.xyz/).

## Content Structure

- `raw/` — Source PDFs processed by pdf-extractor (text + images)
- `content/` — LLM-authored markdown pages (books, concepts, comparisons, cases)
- `.claude/skills/` — LLM tools for content workflows

## LLM Skills

| Skill | Purpose |
|-------|---------|
| `/pdf-extractor <file>` | Extract text + images from PDF into `raw/` |
| `/semantic-chunker <book>` | Split text into chapter-aligned chunks |
| `/wiki-ingest <book> [N]` | Ingest a chunk into content pages |
| `/wiki-query <question>` | Search content and synthesize answers |
| `/wiki-lint [--fix]` | Check quality (--fix auto-fixes inline links + missing links) |
| `/wiki-compare [a] [b]` | Create comparison pages between concepts |
| `/wiki-cases [book\|--url <url>]` | Extract CFT-style cases from books or external sources |

### Skill Workflows

**Ingest a book:**
1. `/pdf-extractor <book.pdf>` — extract PDF to `raw/`
2. `/semantic-chunker <book>` — chunk the text at chapter boundaries
3. `/wiki-ingest <book>` — process chunks into content (repeat for each chunk)
4. `/wiki-lint --fix` — verify and auto-fix quality issues
5. `/wiki-cases <book>` — extract notable cases from the book
6. `npx quartz sync --no-pull` — commit and push to GitHub

**Query the knowledge base:**
1. `/wiki-query <question>` — get synthesized answer
2. Optionally file the answer as a new page

## Content Types

- **Books** — `content/books/` — chapter summaries from ingested sources
- **Concepts** — `content/concepts/` — reusable design ideas, cross-referenced
- **Comparisons** — `content/comparisons/` — tensions and trade-offs between concepts
- **Cases** — `content/cases/` — rich narratives illustrating multiple concepts together

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

See [Quartz docs](https://quartz.jzhao.xyz/setting-up-your-GitHub-repository) for details.
