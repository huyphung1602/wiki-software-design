---
name: wiki-lint
description: Health-check the wiki for orphans, broken links, contradictions, stale claims, and gaps. Use when user invokes /wiki-lint or asks to check wiki quality.
allowed-tools: Read,Write,Edit,Glob,Grep
---

# Wiki Lint Skill

## Role

**Health-check the wiki**

Scans all wiki pages for issues: orphans, missing pages, contradictions, stale claims, missing cross-references, and knowledge gaps.

**Position in flow**: `/wiki-lint` → report + log entry

## Invocation

- `/wiki-lint` — run all checks (report only)
- `/wiki-lint --fix` — run all checks and auto-fix issues where possible

**Fix mode** (`--fix`):
- **Inline link readability (check 12)**: rewrites bare `[[page-name]]` to `[[page-name|inline text]]` where the surrounding sentence has better phrasing
- **Missing cross-references (check 5)**: auto-adds `[[links]]` where a concept name or alias appears in prose without being linked — links the first mention of each concept per page (report-only for check 5 in non-fix mode)

## Checks

### 1. Orphan pages

Scan all wiki pages for `[[page-name]]` references. Build a set of pages with inbound links. Any page in `content/` not in this set (except `index.md`) is an orphan.

### 2. Missing concept pages

Collect all `[[page-name]]` references across the wiki. Check if each referenced page exists in `content/`. Report broken links.

### 3. Contradictions

For each concept page in `content/concepts/`, read pages that share the same `tags` or `sources` in their YAML frontmatter. Compare claims. Flag pairs where one page states something that another contradicts or qualifies differently.

### 4. Stale claims

Check recent git commits for ingested sources. For each recently ingested source, find concept pages that share tags with that source. Flag any that haven't been updated since the ingest date.

### 5. Missing cross-references

For each concept page, check if it mentions related concepts in its text without linking to them. Flag concepts that appear in the text but lack `[[links]]`.

**Fix mode**: Auto-add `[[links]]` for the first mention of each unlinked concept per page. Scan all concept names and their aliases (from frontmatter). For each wiki page, find the first occurrence of each concept name or alias in the prose (excluding YAML frontmatter, code blocks, and already-linked text). If the concept is not yet linked in that page, wrap the mention in `[[link]]`. Be conservative — only link when the concept name/alias appears as a distinct phrase (multi-word aliases as phrases, single-word aliases with word boundaries).

### 6. Knowledge gaps

Identify topics that appear across multiple book sources (check `sources` in YAML frontmatter) but don't have a comparison or synthesis page. Suggest creating one.

### 7. Oversized pages

Check word count of each chapter summary and concept page. Flag chapter summaries significantly over 300 words and concept pages significantly over 500 words.

### 8. Orphan cases

Scan all pages in `content/cases/`. For each case page, check if any concept page in `content/concepts/` has a `## Cases` section linking to it. Cases with no inbound links from concept pages are orphans.

### 9. Missing case links on concept pages

For each concept page, check if `content/cases/` contains cases that include this concept in their `concepts` frontmatter. If cases exist but the concept page has no `## Cases` section, flag it.

### 10. Invalid crossroad field

For each case page, verify the `crossroad` field exists and is a boolean value. Flag any non-boolean values.

### 11. Oversized case pages

Check word count of each case page. Flag cases significantly over 1200 words (soft target ~600 words).

### 12. Inline link readability

For every bare `[[page-name]]` link (no `|` pipe) in wiki content, extract the page name, strip hyphens, and check if the surrounding sentence contains a phrase that describes the concept more naturally than the bare page name.

**The principle**: Like Wikipedia, `[[deep-modules|deep modules]]` reads naturally in prose even though the page is `deep-modules`. A bare `[[page-name]]` link should be rewritten to `[[page-name|inline text]]` when the inline text is already present in the surrounding sentence and reads better.

**Detection algorithm**:
1. Find all `[[page-name]]` with no `|` (bare links)
2. Get the sentence containing the link
3. Strip the page name: `deep-modules` → `deep modules`
4. Find words/phrases near the link in the sentence
5. If the sentence contains a word/phrase that clearly describes the linked concept but differs from the stripped page name, flag it

**Examples**:
- Sentence: "...is **state** — the biggest cause..." → `[[state-and-complexity]]` → suggest `[[state-and-complexity|state]]`
- Sentence: "...use **consistent naming**..." → `[[choosing-names]]` → suggest `[[choosing-names|consistent naming]]`
- Sentence: "...**deep module** example..." → `[[deep-modules]]` → suggest `[[deep-modules|deep module]]`
- Sentence: "...**complexity** breeds..." → `[[complexity]]` → no change needed (stripped name matches)

**Fix mode**: Rewrite the bare link with the contextual phrase found in the sentence. The inline text is taken directly from the sentence text immediately surrounding the link.

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

### Orphan Cases (N)
- [[case-name]] — no concept pages link to it

### Missing Case Links (N)
- [[concept-name]] — has N related cases but no ## Cases section

### Invalid Crossroad Fields (N)
- [[case-name]] — crossroad value is not boolean

### Oversized Case Pages (N)
- [[case-name]] is <word-count> words (target: ~600, max: ~1200)

### Inline Link Readability (N)
- [[page-name]] in [[source-page]] — suggest `[[page-name|inline text]]` (inline text found in surrounding sentence)
```

Present the report in chat only (no file write). In fix mode (`/wiki-lint --fix`), auto-fix inline link readability (check 12) and missing cross-references (check 5).

## What NOT to Do

❌ DO NOT modify any wiki pages during lint (report mode)
❌ DO NOT skip any check
❌ DO NOT modify files in `raw/`

✅ DO report all issues found
✅ DO suggest concrete fixes for each issue
✅ DO auto-fix inline link readability in fix mode
