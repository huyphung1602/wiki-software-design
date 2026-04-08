# LLM Content Schema

You are maintaining a personal knowledge site powered by Quartz. The content has three layers:

1. **raw/** — Immutable source documents (extracted text from PDFs). Never modify these.
2. **content/** — LLM-owned markdown pages. You create and maintain all files here.
3. **CLAUDE.md** — This file. The rules you follow.

**Deployment**: Quartz v4 publishes the `content/` folder as a wiki-style site.

**Tools**: Other tools in `.claude/skills/` handle content generation (pdf-extractor, semantic-chunker) and parsing (wiki-ingest, wiki-query, wiki-lint, wiki-compare).

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
- **Page structure**: H1 title → short intro paragraph → content sections → `## Related` section at bottom with links to related pages.
- **Word targets**: Chapter summaries ~300 words, concept pages ~500 words. Soft targets — wiki-lint flags pages significantly over limit.

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
   - `content/overview.md` — update high-level synthesis
5. Update `content/index.md` — add new pages, update summaries
6. Append to `content/log.md` — format: `## [YYYY-MM-DD] ingest | <book-name> | Ch <N>: <title>`

**Abort/resume**: A chunk is fully ingested only after step 6 (log.md updated). If interrupted, the next ingest re-processes that chunk.

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

Output a report and append to `content/log.md`.

## Guardrails

- NEVER modify files in `raw/`
- ALWAYS update `content/index.md` and `content/log.md` after any content change
- ALWAYS ask before filing a query answer as a new page
- When the user says "process this PDF", chain: pdf-extractor → semantic-chunker → wiki-ingest
