---
name: wiki-compare
description: Scan the wiki for cross-concept tensions, trade-offs, and interactions. Creates and updates comparison pages in content/comparisons/. Use after ingest sessions, lint passes, or when user wants to explore how concepts relate.
allowed-tools: Read,Write,Edit,Glob,Grep,AskUserQuestion
---

# Wiki Compare Skill

## Role

**Detect cross-concept tensions and create/update comparison pages**

Scans the wiki for pairs of concepts that have interesting interactions — tensions, trade-offs, synergies, or conflicts — and creates dedicated comparison pages. This skill is independent from ingest and can be run at any time.

**Position in flow**: `content/concepts/ → wiki-compare → content/comparisons/`

## Invocation

- `/wiki-compare` — scan all concept pages for cross-concept tensions
- `/wiki-compare <concept-a> <concept-b>` — compare two specific concepts
- `/wiki-compare --new-source <book-name>` — focus on tensions involving concepts from a recently ingested source

## What is a Comparison Page?

Comparison pages are for **cross-concept analysis** — situations where two or more distinct concepts interact, conflict, or complement each other. They are NOT for:
- Two sources disagreeing on the same concept (that belongs on the concept page itself, under `## Synthesis`)
- Simple "see also" relationships (that belongs in `## Related` sections)

Good candidates for comparison pages:
- Two design principles that can conflict (e.g., "design it twice" vs "don't repeat yourself")
- A practice and its anti-pattern (e.g., "deep modules" vs "shallow modules")
- Two approaches to the same problem from different angles (e.g., "top-down decomposition" vs "bottom-up composition")
- A concept and its boundary condition (e.g., "information hiding" vs "information leakage")
- **Cross-source tensions**: a concept from one source vs a concept from another (e.g., Ousterhout's "deep modules" vs Martin's "single responsibility principle")

## Types of Comparisons

### Within-source comparisons
Both concepts come from the same book. The comparison captures tensions the author themselves identifies.
- Example: Ousterhout contrasts deep modules vs shallow modules throughout his book
- These often emerge naturally during ingest

### Cross-source comparisons
Each concept originates from a different source. The comparison captures tensions between different schools of thought.
- Example: Ousterhout's "deep modules" (few large modules) vs Martin's "single responsibility" (many small classes)
- These only become possible once multiple sources are ingested
- These are often the most valuable comparisons because they reveal genuine philosophical disagreements

## Step-by-Step

### 1. Gather concept pages

- If comparing specific concepts: read both concept pages (match by title OR `aliases` in frontmatter)
- If `--new-source`: read all concept pages that include the new source in their `sources` frontmatter, plus existing comparison pages
- Otherwise: read all pages in `content/concepts/` and scan for pairs that share tags, appear in each other's `## Related` sections, or discuss overlapping concerns

Also read all existing pages in `content/comparisons/` to avoid duplicating comparisons and to identify pages that need updating.

**Alias awareness**: When comparing concepts, use both `title` and `aliases` from frontmatter for matching. A concept page titled "Information Hiding" with aliases `[encapsulation, data hiding]` should be recognized when a source discusses "encapsulation". Always use the canonical page title (the `title` field) in wiki links and comparison file names.

### 2. Identify tensions (INTERACTIVE — pause here)

Present candidate pairs grouped by type:

```
Found 6 potential comparisons:

New (no existing page):
  1. [[deep-modules]] vs [[shallow-modules]] — principle vs anti-pattern (within-source)
  2. [[strategic-programming]] vs [[technical-debt]] — investment vs cost (within-source)
  3. [[deep-modules]] vs [[single-responsibility]] — few large vs many small modules (cross-source: Ousterhout vs Martin)

Needs update (existing page, new source adds perspective):
  4. [[deep-modules-vs-shallow-modules]] — Clean Code discusses similar tension differently

Ask the user which to pursue. Let them suggest additional pairs.

Wait for user input before proceeding.
```

### 3. Write or update comparison pages

#### Creating a new comparison page

**File naming**: `<concept-a>-vs-<concept-b>.md` (alphabetical order)

**Single-source structure** (both concepts from same source):

```markdown
---
title: Concept A vs Concept B
aliases: [concept-b vs concept-a, <alternate-name-for-this-tension>]
tags: [comparison, tag1, tag2]
sources: [<source>]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Concept A vs Concept B

Brief intro: what these concepts are and why comparing them matters.

## Concept A: <one-sentence definition>

Key characteristics in context of this comparison. Link to [[concept-a]].

## Concept B: <one-sentence definition>

Key characteristics in context of this comparison. Link to [[concept-b]].

## The Tension

Where they conflict, compete, or create hard choices.

## When to Favor Concept A
## When to Favor Concept B

## Related
- [[concept-a]] — full concept page
- [[concept-b]] — full concept page
```

**Cross-source structure** (concepts from different sources):

```markdown
---
title: Concept A vs Concept B
aliases: [concept-b vs concept-a, <alternate-name-for-this-tension>]
tags: [comparison, tag1, tag2]
sources: [<source-a>, <source-b>]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Concept A vs Concept B

Brief intro: what these concepts are and why comparing them matters.
Note that these concepts originate from different sources with different
philosophical foundations.

## Concept A (from <source-a-title>): <one-sentence definition>

Key characteristics. Link to [[concept-a]].

## Concept B (from <source-b-title>): <one-sentence definition>

Key characteristics. Link to [[concept-b]].

## The Tension

Where they conflict or create hard choices. Be explicit about whether
this is a genuine disagreement between sources or a difference in scope.

## When to Favor Concept A
## When to Favor Concept B

## Related
- [[concept-a]] — full concept page
- [[concept-b]] — full concept page
```

#### Updating an existing comparison page (new source adds perspective)

When a new source discusses the same tension:
- **Restructure** using the same pattern as concept pages
- Move existing content under `## In <first-source-title>`
- Add new perspective under `## In <new-source-title>`
- Add or update `## Synthesis` section noting how sources agree or differ on this tension
- Append new source to `sources` array in frontmatter

Example — before (single source):
```markdown
## The Tension
Deep modules maximize the ratio of functionality to interface cost.
Shallow modules fail at this...
```

After (second source added):
```markdown
## In A Philosophy of Software Design
Deep modules maximize the ratio of functionality to interface cost.
Shallow modules fail at this...

## In Clean Code
Martin approaches this from the angle of class size, arguing that...

## Synthesis
Both authors value simplicity but define it differently: Ousterhout
measures simplicity at the interface level (few methods), while Martin
measures it at the class level (single responsibility). These can
conflict — a class with a single responsibility may still have a
complex interface relative to its functionality.
```

### 4. Update index and log

Update `content/index.md`:
- Add new comparison pages under the Comparisons category
- Update source counts on existing comparison entries

Append to `content/log.md`:
```markdown
## [YYYY-MM-DD] compare | cross-concept
- Created: [[comparison-a-vs-b]], [[comparison-c-vs-d]]
- Updated: [[comparison-e-vs-f]]
- Updated: [[index]]
```

### 5. Update related concepts

Add a link to the comparison page in the `## Related` section of each concept page involved:
- `- [[concept-a-vs-concept-b]] — tension between these approaches`

For cross-source comparisons, add the link to both concept pages regardless of source.

## What NOT to Do

❌ DO NOT create comparison pages for same-concept source disagreements (use concept page `## Synthesis`)
❌ DO NOT create comparison pages without user approval
❌ DO NOT modify files in `raw/`
❌ DO NOT duplicate existing comparisons — check `content/comparisons/` first

✅ DO present candidates and let the user choose
✅ DO update index.md and log.md after creating/updating pages
✅ DO add cross-references back to the comparison from concept pages
✅ DO link to full concept pages from within comparisons
✅ DO look for cross-source comparisons when multiple sources exist
✅ DO check existing comparison pages for update opportunities when new sources are ingested
