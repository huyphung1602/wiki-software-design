---
name: wiki-cases
description: Extract and manage CFT-style cases — rich, multi-conceptual narratives from books and external sources. Creates cases in content/cases/ with fragment tagging. Use after wiki-ingest or when user invokes /wiki-cases.
allowed-tools: Read,Write,Edit,Glob,Grep,AskUserQuestion
---

# Wiki Cases Skill

## Role

**Extract and manage CFT-style cases**

Creates rich, multi-conceptual case pages following Cognitive Flexibility Theory. Cases are first-class wiki citizens — not disposable examples. Each case is a whole narrative that illustrates multiple concepts through fragments.

**Position in flow**: `content/concepts/ + raw/<book>/chunks/ + external URLs → wiki-cases → content/cases/`

## Invocation

- `/wiki-cases <book-name>` — scan raw chunks from an ingested book for case-worthy narratives
- `/wiki-cases --url <url>` — extract a case from an external article/blog post
- `/wiki-cases` — scan all existing content for crossroad case candidates
- `/wiki-cases --concept <concept-name>` — find cases relevant to a specific concept

## What Is a Case

A case is a **rich, multi-conceptual narrative** grounded in Cognitive Flexibility Theory:

- **First-class citizen** — as important as concepts, not subordinate to them
- **Multi-conceptual** — one case illustrates many concepts simultaneously
- **Fragmentable** — different sections illuminate different concepts
- **Variable** — the same concept looks wildly different across cases
- **Crossroad-worthy** — the richest cases become hubs connecting many concepts

The learning pattern is: **case → concept → other case → other concept** (criss-crossing).

## What Counts as a Case

- A concrete example an author uses to illustrate multiple concepts
- A real-world system/project discussed as an example
- A code snippet used as a teaching example
- A war story or anecdote with a lesson
- An external case study from articles, blog posts, or interviews

## Step-by-Step: Book-Sourced Cases (`/wiki-cases <book-name>`)

### 1. Gather source material

- Read chunk files from `raw/<book>/chunks/`
- Read existing pages in `content/cases/` to avoid duplicates
- Read relevant concept pages in `content/concepts/`

### 2. Identify cases (INTERACTIVE — pause here)

Present candidates to the user:

```
Found 4 potential cases:

  1. UNIX I/O interface as deep module example (from A Philosophy of Software Design)
     → Illustrates: [[deep-modules]], [[information-hiding]]

  2. TCL/TK design decision — two-level vs one-level
     → Illustrates: [[design-it-twice]], [[deep-modules]]

Which cases should we create? You can also suggest your own.
```

Wait for user input before proceeding.

### 3. Write case pages

Create in `content/cases/` using the case page structure (see below).

**Naming**: lowercase-kebab-case derived from the title. Collision handling: append source disambiguator (e.g., `unix-io-deep-module-ousterhout.md`). Multi-source cases use the most descriptive name without a qualifier.

**Word target**: ~600 words soft target. `## The Story` should be concise — capture the essence, not reproduce the full source.

### 4. Update concept pages

Add or append to `## Cases` section on each relevant concept page. This section goes **above** `## Related`:

```markdown
## Cases
- [[case-name]] — brief description of the case (from <source>)

## Related
- [[related-concept]] — explanation
```

If the concept page has no `## Cases` section, add it before `## Related`. If it has no `## Related` either, add `## Cases` at the end.

### 5. Update index and log

Add new case pages to `content/index.md` under a **Cases** category.

Append to `content/log.md`:
```markdown
## [YYYY-MM-DD] cases | <book-name> | <case-title>
- Created: [[case-a]], [[case-b]]
- Updated: [[concept-x]], [[concept-y]], [[index]]
```

### 6. Ask about next steps

Tell the user which cases were created and ask if they want to continue with more cases or run crossroad scanning.

## Step-by-Step: External-Source Cases (`/wiki-cases --url <url>`)

### 1. Fetch the article

Use `mcp__web_reader__webReader` tool. On failure (404, paywall, non-text content), report error to user and offer retry or manual paste.

### 2. Identify the narrative and concepts

Analyze the fetched content for case-worthy stories and the concepts they illustrate.

### 3. Present to user for review (INTERACTIVE)

Show the proposed case structure, fragments, and concept links. Wait for approval.

### 4. Create case page

Write to `content/cases/` with fragments and multi-concept tagging.

### 5. Update concept pages

Add or append to `## Cases` section on relevant concept pages.

### 6. Update index and log

Add to `content/index.md` under Cases category. Append to `content/log.md`.

## Step-by-Step: Crossroad Scanning (`/wiki-cases`)

### 1. Read all existing case pages

Scan `content/cases/` for all case pages.

### 2. Identify crossroad candidates

Rank by number of concepts in `concepts` frontmatter, number of fragment sections, and number of cross-links.

### 3. Present to user (INTERACTIVE)

Suggest `crossroad: true` flags for the top candidates. Wait for approval.

### 4. Update case pages

Set `crossroad: true` in frontmatter for approved cases.

### 5. Update log

Append to `content/log.md`.

## Step-by-Step: Concept-Based Search (`/wiki-cases --concept <concept>`)

### 1. Read the concept page

Find and read the concept page in `content/concepts/`. Use `aliases` frontmatter for matching.

### 2. Search for related cases

Scan raw chunks and existing case pages for narratives that illustrate this concept.

### 3. Present candidates (INTERACTIVE)

Show cases found and offer to create new case pages or link existing ones.

### 4. Create/link cases and update concept pages

Same as book-sourced workflow steps 3-5.

## Case Page Structure

```markdown
---
title: Case Title Here
tags: [case, tag1, tag2]
concepts: [concept-a, concept-b, concept-c]
sources: [book-name-or-url-slug]
crossroad: false
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Case Title Here

## The Story
The full narrative — what happened, what was built, what decision
was made. Keep concise (~200 words).

## Fragments

### Fragment Title
Description of this aspect of the case and what it illustrates.
Illustrates: [[concept-a]], [[concept-b]]

### Another Fragment
Description of another aspect.
Illustrates: [[concept-c]]

## Related Cases
- [[related-case-a]] — brief description of connection
- [[related-case-b]] — brief description of connection

## Source
- [[book-name-chNN]] — source chapter
- [External Article Title](url) — for external sources
```

## Multi-Source Cases

When a new source discusses the same real-world example as an existing case:

- Move existing `## The Story` content under `## In <first-source-title>`
- Add new perspective under `## In <new-source-title>`
- Add or update `## Synthesis` section
- Append new source to `sources` array in frontmatter

## Abort/Resume

A case is fully created only after its entry appears in `content/log.md`. If interrupted:

1. Next invocation reads `content/log.md` to find the last completed case
2. Scans `content/cases/` for pages not yet logged
3. Resumes from the concept page update step for incomplete cases

## What NOT to Do

❌ DO NOT create case pages without user approval
❌ DO NOT modify files in `raw/`
❌ DO NOT treat disposable examples as cases — cases must be rich, multi-conceptual narratives
❌ DO NOT create single-concept cases — if it only illustrates one concept, it belongs in the concept page itself
❌ DO NOT write log.md before all case pages and concept updates are complete

✅ DO present candidates and let the user choose
✅ DO update index.md and log.md after creating/updating pages
✅ DO add cross-references from concept pages back to cases
✅ DO look for crossroad case candidates
✅ DO fragment cases by concept for schema assembly
```