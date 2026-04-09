---
name: wiki-query
description: Search the wiki and synthesize answers with citations. Use when user invokes /wiki-query or asks a question about wiki content.
allowed-tools: Read,Glob,Grep,AskUserQuestion
---

# Wiki Query Skill

## Role

**Search wiki and synthesize answers**

Finds relevant wiki pages and synthesizes a comprehensive answer with citations.

**Position in flow**: `question → wiki-query → synthesized answer (optionally filed as new page)`

## Invocation

- `/wiki-query <question>`

## Step-by-Step

### 1. Find relevant pages

- Read `content/index.md` to identify pages related to the question
- Scan page titles, summaries, and tags for relevance
- Read all relevant wiki pages

### 2. Synthesize answer

- Combine information from multiple pages
- Include `[[wiki links]]` to source pages for every claim
- Note where sources agree or disagree
- Note where information is incomplete (potential gap)

### 3. Present answer to user

Present the synthesized answer. Then ask:

> "Would you like me to file this answer as a new wiki page? It could be a concept page or comparison page."

### 4. Optionally file as new page

If user says yes:
- Create the new page in the appropriate directory (`content/concepts/` or `content/comparisons/`)
- Update `content/index.md`

## What NOT to Do

❌ DO NOT file an answer as a page without asking
❌ DO NOT modify files in `raw/`
❌ DO NOT fabricate information not in the wiki

✅ DO cite wiki pages with `[[links]]`
✅ DO note gaps in the wiki's knowledge
✅ DO update index.md if a new page is created
