---
title: "Chapter 15 - Write The Comments First"
tags: [chapter, software-design, documentation, process]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Chapter 15 - Write The Comments First

Part of [[a-philosophy-of-software-design]]

Most developers delay [[comments-and-documentation|documentation]] until after coding and testing. This is one of the surest ways to produce poor documentation. Comments written at the end repeat the code (because you look at code to write them), miss important design rationale (because you've forgotten it), and often never get written at all (because the backlog becomes daunting).

The [[comments-first-approach|comments-first approach]]: write class interface comments first, then method interface comments and signatures (with empty bodies), iterate until the structure feels right, then instance variables, then fill in method bodies. When code is done, comments are done. No backlog.

Three benefits:
1. **Better comments** — Design issues are fresh in mind. You focus on abstraction without implementation distraction. Comments improve during coding as you notice and fix problems.
2. **Better design** — Comments are the only way to fully capture [[abstractions|abstraction]]. Writing them early lets you review and tune before writing code. Comments serve as a "canary in the coal mine" — if a method needs a long, complicated interface comment, the interface is too complex. If you can't describe it simply and completely, the design needs work.
3. **More fun** — Designing abstractions is the most enjoyable part of programming. Comments are how you record and evaluate design quality. Finding simple, clear comments is a source of pride.

The cost argument is weak: writing comments accounts for ~5% of development time. Writing them first may actually save time by stabilizing abstractions before coding, reducing code revisions.

## Related
- [[comments-and-documentation]] — the role of comments
- [[comments-first-approach]] — the process of writing comments first
- [[abstractions]] — what early comments capture
- [[deep-modules]] — simplicity of interface comment indicates depth
