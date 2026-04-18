---
title: "Chapter 18 - Code Should be Obvious"
tags: [software-design, readability, code-quality]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Chapter 18 - Code Should be Obvious

Part of [[a-philosophy-of-software-design]]

[[obvious-code|Obvious code]] can be read quickly, without much thought, and the reader's first guess about its behavior will be correct. This chapter addresses obscurity, one of the two root causes of [[complexity]], by identifying what makes code more or less obvious.

## Making Code More Obvious

Two major techniques have been covered earlier: [[choosing-names|choosing good names]] and [[consistency|applying consistency]]. Beyond those, judicious use of whitespace helps -- blank lines separate major code blocks, spacing within statements clarifies structure, and parameter documentation should be formatted so parameters are visually distinct. When code cannot be made obvious through structure, comments must fill the gap by providing the information a reader would otherwise lack.

## What Makes Code Less Obvious

Several patterns create obscurity: event-driven programming obscures control flow because handlers are invoked indirectly; generic containers like `Pair` hide meaning behind names like `getKey()` and `getValue()`, so dedicated structures with meaningful names are better; declaring a variable with one type but allocating it as a subtype misleads readers; and code that violates reader expectations (like a constructor that spawns background threads) must be explicitly documented. The chapter reinforces a general rule: software should be designed for ease of reading, not ease of writing.

## The Information View

Nonobvious code means readers lack important information. Three remedies: reduce the information needed through [[abstractions|abstraction]] and eliminating special cases; leverage information readers already have through conventions and expectations; and present essential information through good names and strategic comments. Code reviews are the best tool for detecting nonobviousness, since it is easier to spot in others' code than your own.

## Related
- [[obvious-code]] -- the concept page for this chapter's core idea
- [[consistency]] -- a primary technique for making code obvious
- [[choosing-names]] -- precise names reduce obscurity
- [[comments-and-documentation]] -- compensating for unavoidable nonobviousness
- [[complexity]] -- obscurity as a root cause
- [[red-flags]] -- nonobvious code is itself a red flag
