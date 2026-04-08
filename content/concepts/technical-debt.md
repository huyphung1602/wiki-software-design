---
title: Technical Debt
aliases: [tech debt, design debt]
tags: [metaphor, complexity, cost]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Technical Debt

Technical debt is the common metaphor for the problems caused by [[tactical-programming|tactical programming]]. By programming tactically, you borrow time from the future: development goes faster now, but slower later.

Ousterhout adds an important nuance: **unlike financial debt, most technical debt is never fully repaid.** You don't just pay interest — you keep paying the principal forever. Once a code base has accumulated enough [[complexity]], it becomes nearly impossible to fix. The system degrades irreversibly.

This makes technical debt more dangerous than the financial analogy suggests. Financial debt can be calculated and managed. Technical debt is insidious — each small compromise seems reasonable in isolation, but together they create a death spiral where every change takes longer, which leads to more shortcuts, which creates more complexity.

The solution is not to "pay down" debt in large batches (that rarely happens). It's to adopt a [[design-investment|continuous investment]] approach: make small design improvements with every change so debt never accumulates to catastrophic levels.

## Related
- [[complexity]] — what technical debt is made of
- [[strategic-vs-tactical-programming]] — tactical programming creates debt, strategic prevents it
- [[design-investment]] — the continuous approach to managing debt
- [[a-philosophy-of-software-design-ch03]] — where Ousterhout discusses this
