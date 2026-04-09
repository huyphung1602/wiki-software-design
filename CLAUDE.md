# LLM Content Schema

You are maintaining a personal knowledge site powered by Quartz. The content has three layers:

1. **raw/** — Immutable source documents (extracted text and images from PDFs). Never modify these (exception: pdf-extractor creates and may overwrite `raw/` content during extraction).
2. **content/** — LLM-owned markdown pages. You create and maintain all files here.
3. **CLAUDE.md** — This file. The rules you follow.

**Deployment**: Quartz v4 publishes the `content/` folder as a wiki-style site. `content/index.md` is the home page — it includes the wiki overview/About section at the top, followed by lists of all Books, Concepts, and Comparisons.

**Tools**: Other tools in `.claude/skills/` handle content generation (pdf-extractor, semantic-chunker) and parsing (wiki-ingest, wiki-query, wiki-lint, wiki-compare, wiki-cases).

## Content Conventions

- **File naming**: lowercase-kebab-case (e.g., `solid-principles.md`, `design-patterns-ch01.md`)
- **YAML frontmatter** on every page:
  ```yaml
  ---
  title: Page Title
  tags: [tag1, tag2]
  sources: [book-name]
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  ---
  ```
- **Linking**: First mention of a concept per page is always a `[[wiki-link]]`. Subsequent mentions can be plain text.
- **Page structure**: H1 title → short intro paragraph → content sections → `## Cases` section (for concept pages) → `## Related` section at bottom with links to related pages.
- **Word targets**: Chapter summaries ~300 words, concept pages ~500 words, case pages ~600 words. Soft targets — wiki-lint flags pages significantly over limit.

## Workflows

### Ingest Workflow

Triggered by: `/wiki-ingest <book-name> [chunk-number]`

1. Read the chunk from `raw/<book-name>/chunks/` and its entry in `raw/<book-name>/map.md`
2. If this chunk continues a chapter from a previous chunk, read the prior chunk(s) for context
3. Present key takeaways to the user, discuss what to emphasize
4. Write/update content pages:
   - `content/books/<book-name>-<chapter>.md` — chapter summary (write when last chunk for chapter is reached)
   - `content/books/<book-name>.md` — update book overview
   - `content/concepts/<concept>.md` — create or update for each concept mentioned
   - `content/comparisons/` — note contradictions or reinforcements with existing ideas
5. Update `content/index.md` — add new pages, update summaries

### Query Workflow

Triggered by: `/wiki-query <question>`

1. Read `content/index.md` to find relevant pages
2. Read relevant content pages
3. Synthesize answer with `[[wiki links]]` to source pages
4. Ask user if they want the answer filed as a new page

### Lint Workflow

Triggered by: `/wiki-lint`

Check for:
- **Orphan pages**: Pages with no inbound `[[links]]` from other pages
- **Missing concept pages**: `[[links]]` pointing to pages that don't exist
- **Contradictions**: Concept pages sharing tags/sources where claims conflict
- **Stale claims**: Concept pages sharing tags with recently ingested sources but not updated
- **Missing cross-references**: Concept pages mentioning related concepts without linking
- **Knowledge gaps**: Topics across multiple sources lacking a synthesis/comparison page

Output a report in chat.

### Cases Workflow

Triggered by: `/wiki-cases <book-name>`, `/wiki-cases --url <url>`, or `/wiki-cases`

1. Scan raw chunks or fetch external article for case-worthy narratives
2. Present candidates to the user for selection (interactive)
3. Create case pages in `content/cases/` with fragments and multi-concept tagging
4. Update concept pages — add `## Cases` section linking to new cases
5. Update `content/index.md`

**When to run**: After wiki-ingest finishes a book, or anytime for external sources.

## Guardrails

- NEVER modify files in `raw/` (exception: pdf-extractor creates and may overwrite `raw/` content during extraction)
- ALWAYS update `content/index.md` after any content change
- ALWAYS ask before filing a query answer as a new page
- When the user says "process this PDF", chain: pdf-extractor → semantic-chunker → wiki-ingest
