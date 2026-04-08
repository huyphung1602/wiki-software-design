---
name: wiki-lint
description: Health-check the wiki for orphans, broken links, contradictions, stale claims, and gaps. Use when user invokes /wiki-lint or asks to check wiki quality.
allowed-tools: Read,Write,Glob,Grep
---

# Wiki Lint Skill

## Role

**Health-check the wiki**

Scans all wiki pages for issues: orphans, missing pages, contradictions, stale claims, missing cross-references, and knowledge gaps.

**Position in flow**: `/wiki-lint` → report + log entry

## Invocation

- `/wiki-lint` — run all checks

## Checks

### 1. Orphan pages

Scan all wiki pages for `[[page-name]]` references. Build a set of pages with inbound links. Any page in `content/` not in this set (except `index.md` and `log.md`) is an orphan.

### 2. Missing concept pages

Collect all `[[page-name]]` references across the wiki. Check if each referenced page exists in `content/`. Report broken links.

### 3. Contradictions

For each concept page in `content/concepts/`, read pages that share the same `tags` or `sources` in their YAML frontmatter. Compare claims. Flag pairs where one page states something that another contradicts or qualifies differently.

### 4. Stale claims

Check `content/log.md` for recently ingested sources. For each recent ingest, find concept pages that share tags with the new source. Flag any that haven't been updated since the ingest date.

### 5. Missing cross-references

For each concept page, check if it mentions related concepts in its text without linking to them. Flag concepts that appear in the text but lack `[[links]]`.

### 6. Knowledge gaps

Identify topics that appear across multiple book sources (check `sources` in YAML frontmatter) but don't have a comparison or synthesis page. Suggest creating one.

### 7. Oversized pages

Check word count of each chapter summary and concept page. Flag chapter summaries significantly over 300 words and concept pages significantly over 500 words.

## Output

Present a structured report in chat:

```markdown
## Wiki Lint Report — YYYY-MM-DD

### Orphan Pages (N)
- [[page-name]] — no inbound links

### Broken Links (N)
- [[missing-page]] referenced in [[source-page]]

### Contradictions (N)
- [[concept-a]] vs [[concept-b]]: <description of conflict>

### Stale Claims (N)
- [[concept-c]] not updated since <source> was ingested

### Missing Cross-References (N)
- [[concept-d]] mentions X without linking to [[x]]

### Knowledge Gaps (N)
- <topic> appears in <N> sources but has no comparison page

### Oversized Pages (N)
- [[page-name]] is <word-count> words (target: <target>)
```

Then append to `content/log.md`:

```markdown
## [YYYY-MM-DD] lint | full check
- Orphans: N | Broken links: N | Contradictions: N | Stale: N | Missing refs: N | Gaps: N | Oversized: N
```

## What NOT to Do

❌ DO NOT modify any wiki pages during lint
❌ DO NOT skip any check
❌ DO NOT modify files in `raw/`

✅ DO report all issues found
✅ DO suggest concrete fixes for each issue
✅ DO append results to log.md
