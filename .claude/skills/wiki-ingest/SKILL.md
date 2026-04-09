---
name: wiki-ingest
description: Ingest a book chunk into the wiki. Use when user invokes /wiki-ingest or wants to process book content into wiki pages. Interactive — pauses for user discussion before writing.
allowed-tools: Bash,Read,Write,Edit,Glob,Grep,AskUserQuestion
---

# Wiki Ingest Skill

## Role

**Interactive chunk → wiki pages**

Reads one chunk at a time, discusses key takeaways with the user, then creates/updates wiki pages. This is the core skill for building the knowledge base.

**Position in flow**: `raw/<book>/chunks/*.md → wiki-ingest → content/ pages`

## Invocation

- `/wiki-ingest <book-name>` — ingest the next uningested chunk (checks log.md for progress)
- `/wiki-ingest <book-name> <chunk-number>` — ingest a specific chunk

## Step-by-Step

### 1. Determine which chunk to ingest

- If chunk number specified: read that chunk
- Otherwise: scan `content/log.md` for the last ingested chunk of this book, then read the next one
- Read `raw/<book-name>/map.md` to get the chapter mapping for this chunk

### 2. Read and analyze the chunk

- Read `raw/<book-name>/chunks/chunk-NNN.md`
- If map.md shows this chunk continues a chapter from a previous chunk, also read the prior chunk(s)
- Identify key concepts, arguments, and takeaways

### 2b. Handle images (if present)

If the chunk text contains `[Image: page-NNN-img-MM.ext]` placeholders:

1. For each placeholder, read the image file from `raw/<book-name>/images/` using the Read tool (which supports images)
2. Generate a description of the image content (diagrams, charts, code, etc.)
3. **CRITICAL: Images must stay inline where the placeholder appears in the chunk text.** The placeholder `[Image: ...]` is already positioned near the relevant content — keep the image reference there.
4. Copy the image file from `raw/<book-name>/images/` to `content/images/<book-name>/` (preserve original filename)
5. Replace the placeholder with the image reference: `![Description](../images/<book-name>/page-NNN-img-MM.ext)`
   - Use the description from step 2 in the alt text
6. If the image file doesn't exist or can't be read, replace with `[Image could not be extracted]`
7. **DO NOT create a separate `## Images` section** — all images must remain inline with their relevant content

**Image directory structure:**
- Source: `raw/<book-name>/images/page-NNN-fig-XX.png`
- Destination: `content/images/<book-name>/page-NNN-fig-XX.png`
- Reference: `../images/<book-name>/page-NNN-fig-XX.png` (relative from content/books/)

The user will see image descriptions during the interactive discussion (step 3) and can correct or refine them.

### 3. Present to user (INTERACTIVE — pause here)

Present a summary of the chunk's key takeaways to the user. Ask:
- What to emphasize
- Which concepts deserve their own pages
- Any connections to existing wiki content the user notices

Wait for user input before proceeding.

### 4. Write wiki pages

Based on the discussion:

**Chapter summary page** (`content/books/<book-name>-chNN.md`):
- Write when the last chunk for a chapter is reached (check map.md)
- For multi-chunk chapters: accumulate understanding, write only when complete
- Include YAML frontmatter, ~300 words, `[[wiki links]]` for concepts
- Link back to book overview: `Part of [[<book-name>]]`
- **Structure**: H1 title → 2-4 paragraphs flowing prose → `Part of [[...]]` → `## Related`
- **Use bold section markers for key topics** (`**Topic.**` at paragraph start), NOT `##` headers
- **No tables** — convert table content to prose descriptions
- **No subsections with ## headers** — chapter summaries are single-section prose
- The summary should capture ALL key points from the chapter, but in concise prose form

**Book overview page** (`content/books/<book-name>.md`):
- Create on first chunk, update on subsequent chunks
- High-level summary, list of chapters with links, key themes

**Concept pages** (`content/concepts/<concept>.md`):

**Alias matching** — Before creating a new concept page, check if the concept already exists under a different name:
1. Scan all existing concept pages' `aliases` fields in frontmatter
2. If the chunk's concept matches an alias, treat it as an existing concept (update, don't create)
3. During the interactive discussion (step 3), flag potential alias matches to the user for confirmation
4. If confirmed as an alias, add the new name to the existing page's `aliases` array

When the concept is **new** (no existing page or alias match):
- Create the page with single-source content
- Structure: `# Title` → definition/prose → `## Related`
- Set `sources: [<current-book>]` in frontmatter
- Add `aliases` in frontmatter with alternate names from this source (if any)

When the concept **already exists** (second or later source):
- **Restructure** the page — do NOT just append to existing prose
- Move the existing single-source content under a `## In <first-book-title>` heading
- Add the new source's perspective under a `## In <current-book-title>` heading
- Add a `## Synthesis` section noting agreements, tensions, and open questions between sources
- Append the new source to the `sources` array in frontmatter (e.g., `sources: [book-a, book-b]`)
- Add new `## Related` links pointing to chapters from the new source
- Preserve all existing content — layer on top, don't rewrite

The `sources` frontmatter array tracks all contributing sources — this enables filtering via Dataview queries.

**Restructure example:**

Before (single source):
```markdown
---
title: Information Hiding
aliases: [encapsulation, data hiding]
tags: [core-concept, modules, design, encapsulation]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Information Hiding

Information hiding is the primary technique for achieving [[deep-modules]]...

## Related
- [[deep-modules]] — what information hiding produces
- [[a-philosophy-of-software-design-ch05]] — where this is developed
```

After (second source added):
```markdown
---
title: Information Hiding
aliases: [encapsulation, data hiding, information encapsulation]
tags: [core-concept, modules, design, encapsulation]
sources: [a-philosophy-of-software-design, clean-code]
created: 2026-04-08
updated: 2026-04-10
---

# Information Hiding

## In A Philosophy of Software Design

Information hiding is the primary technique for achieving [[deep-modules]]...

## In Clean Code

Martin uses the term "encapsulation" to describe a similar idea,
focusing on...

## Synthesis

Both authors value hiding implementation details, but differ in emphasis:
Ousterhout focuses on hiding *design decisions* (knowledge), while
Martin focuses on hiding *data* (state). These are complementary —
a module can hide both well or fail at either.

## Related
- [[deep-modules]] — what information hiding produces
- [[a-philosophy-of-software-design-ch05]] — where this is developed
- [[clean-code-ch04]] — where encapsulation is discussed
```

**Comparison pages** (`content/comparisons/`):

When the chunk discusses a concept that already has a comparison page:
- If the new source adds a perspective on the same tension (e.g., another author discussing depth vs shallowness): restructure the comparison page using the same `## In <book>` + `## Synthesis` pattern as concept pages
- Append the new source to the `sources` array in frontmatter

Do NOT create new comparison pages during ingest — that's the wiki-compare skill's job. Only update existing ones if the chunk directly addresses a known tension.

**Overview page** (`content/overview.md`):
- Update the high-level synthesis with new themes or connections

### 5. Update index

Update `content/index.md`:
- Add new pages under the appropriate category (Books, Concepts)
- Update page counts and source counts on existing entries

### 6. Update log

Append to `content/log.md`:
```markdown
## [YYYY-MM-DD] ingest | <book-name> | Ch <N>: <title>
- Created: [[page-a]], [[page-b]]
- Updated: [[overview]], [[index]]
```

### 7. Ask about next chunk

Tell the user which chunk was just ingested and ask if they want to continue with the next one.

## Obsidian Linking Rules

- First mention of a concept per page: `[[concept-name]]`
- Subsequent mentions: plain text
- Chapter pages link back to book: `Part of [[book-name]]`
- Concept pages link to source chapters: `Discussed in [[book-name-ch01]]`
- All pages end with `## Related` section linking to connected pages

## What NOT to Do

❌ DO NOT skip the interactive discussion (step 3)
❌ DO NOT modify files in `raw/`
❌ DO NOT write log.md before all wiki pages are written (breaks resume)
❌ DO NOT proceed to next chunk without user confirmation

✅ DO pause for user input after presenting takeaways
✅ DO update index.md and log.md after every chunk
✅ DO use `[[wiki links]]` liberally
✅ DO check if concept pages already exist before creating new ones
