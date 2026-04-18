---
title: "Chapter 1 - Introduction"
tags: [chapter, introduction]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Chapter 1 - Introduction

Part of [[a-philosophy-of-software-design]]

## Summary

The greatest limitation in software development is our ability to understand the systems we create. As programs grow, [[complexity]] accumulates — subtle dependencies between components make it harder to keep all relevant factors in mind. This slows development and causes bugs.

### Two Approaches to Complexity

1. **Eliminate it**: Make code simpler and more obvious — remove special cases, use consistent naming, simplify logic
2. **Encapsulate it**: Use [[modular-design]] so programmers can work on one module without understanding all others

### Design is Continuous

Software design is not a phase — it's a [[continuous-design]] process spanning the system's entire life. The waterfall model fails because large software systems are too complex to visualize completely upfront. Incremental approaches work because software is malleable enough for mid-course corrections. Developers should always be thinking about design and spending time on design improvements.

### Red Flags

The book introduces **[[red-flags]]** — heuristics for recognizing when code is more complicated than it needs to be. When you spot one, stop and explore alternate designs. The best way to develop design skill is to practice spotting red flags during code reviews.

### Moderation

Every rule has exceptions. Taking any principle to its extreme leads to bad outcomes. Good design balances competing ideas.

## Related
- [[complexity]] — the problem this chapter frames
- [[modular-design]] — encapsulating complexity
- [[continuous-design]] — design as ongoing activity
- [[red-flags]] — spotting design problems
- [[strategic-vs-tactical-programming]] — the mindset shift the book advocates
