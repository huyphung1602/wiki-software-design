---
title: "Ch 14: Choosing Names"
tags: [chapter, software-design, naming]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Ch 14: Choosing Names

Part of [[a-philosophy-of-software-design]]

[[choosing-names|Name choice]] is one of the most underrated aspects of software design. Good names are a form of documentation; poor names increase [[complexity]] incrementally. A bug in the Sprite OS took six months to trace to a variable named `block` used for both physical disk blocks and logical file blocks.

Names should create a clear image of the entity. Two properties: **precision** (not too generic — `numActiveIndexlets` not `getCount()`) and **consistency** (use the same name for the same concept everywhere, never reuse it for different concepts). Boolean names should be predicates. If a precise name is hard to find, that's a [[red-flags|red flag]] suggesting a design problem.

Avoid extra words that don't add information (`fileObject` is redundant). Don't include type information (Hungarian notation is obsolete with modern IDEs). Ousterhout disagrees with Go's ultra-short naming culture, where ambiguous single-character names invite confusion.

The rule: the greater the distance between declaration and use, the longer the name should be. Short names are fine when all uses are visible (loop variables). Choose names as an investment — extra time upfront saves debugging time later, and the skill becomes effortless with practice.

## Related
- [[choosing-names]] — the comprehensive concept
- [[comments-and-documentation]] — names as documentation
- [[red-flags]] — vague name, hard to pick name
