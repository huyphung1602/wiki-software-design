---
title: Choosing Names
aliases: [naming conventions, naming]
tags: [core-concept, naming, design, readability]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Choosing Names

Name choice is one of the most underrated aspects of software design. Good names are a form of documentation: they make code easier to understand, reduce the need for other documentation, and help detect errors. Poor names increase [[complexity]] incrementally — each mediocre name has small impact, but thousands of variables compound the effect.

A name should create a clear image of the underlying entity. The goal: if someone sees the name in isolation, can they guess what it refers to? Names are a form of [[abstractions|abstraction]] — they provide a simplified way of thinking about a complex entity.

Two properties of good names:

**Precision.** The most common problem is names that are too generic or vague. `block` (physical or logical?), `getCount()` (count of what?), `x` and `y` (pixel position or text position?). Boolean names should always be predicates (`cursorVisible`, not `blinkStatus`). If it's hard to find a precise name, that's a [[red-flags|red flag]] suggesting the variable may not have a clean design.

**Consistency.** For common usages, pick one name and use it everywhere. Three requirements: always use the common name for the purpose, never use it for anything else, and ensure the purpose is narrow enough that all variables with the name behave the same. When you need multiple variables of the same type, use the common name with distinguishing prefixes (`srcFileBlock`, `dstFileBlock`).

Avoid extra words. Every word should provide useful information. `fileObject` is redundant (are there files that aren't objects?). Type information in names (Hungarian notation) is unnecessary with modern IDEs. But don't go too short either — Ousterhout disagrees with Go's single-character naming culture, where `ch` means character or channel, `d` means data, difference, or distance.

The greater the distance between a name's declaration and its uses, the longer the name should be. Short names (`i`, `j`) are fine for loops where all uses are visible.

## Related
- [[comments-and-documentation]] — names as a form of documentation
- [[complexity]] — what poor naming incrementally increases
- [[red-flags]] — vague name, hard to pick name
- [[a-philosophy-of-software-design-ch14]] — where naming principles are developed
- [[consistency]] — consistent naming as a primary form of consistency
- [[obvious-code]] — precise names reduce obscurity
- [[decide-what-matters]] — names should convey what matters most
