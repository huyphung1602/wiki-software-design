---
title: Strategic vs Tactical Programming
aliases: [tactical vs strategic programming, investment vs short-term thinking]
tags: [comparison, programming-approach, investment, complexity]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Strategic vs Tactical Programming

The most important mindset decision a developer makes: optimize for the current task, or optimize for the long-term health of the system. This comparison explores the fundamental tension between getting things done quickly and building a sustainable codebase.

## Strategic Programming: invest in good design

The primary goal is to produce a great design, which also happens to work. You invest time proactively (finding simpler designs, writing documentation) and reactively (fixing design problems when discovered). Spend [[design-investment|10–20% of development time]] on these investments. Payback comes in 6–18 months, after which past benefits cover future costs. See [[strategic-programming]] for the full concept.

## Tactical Programming: get it working fast

The main focus is finishing the current task as quickly as possible. You don't spend time looking for the best design — just something that works now. Each quick fix adds a bit of complexity, and you tell yourself it's a reasonable compromise. But complexities accumulate rapidly and compound. See [[tactical-programming]] for the full concept.

## The Tension

The two approaches produce opposite trajectories:

- **Tactical**: fast initial progress, then steadily decelerating as [[complexity]] accumulates. Each feature takes longer than the last.
- **Strategic**: slightly slower at first (10–20% overhead), then accelerating as a clean design makes future work easier.

The crossover point is roughly 6–18 months. After that, strategic programmers are at least 10–20% faster than they would have been tactically — and the gap keeps growing.

The trap: tactical programming *feels* productive. You're shipping features quickly. But you're borrowing time from the future. The resulting [[technical-debt]] is like financial debt where the interest compounds — except unlike financial debt, most tech debt is never fully repaid.

Real-world example: Facebook's original motto was "Move fast and break things" — pure tactical culture. Engineers pushed commits to production in their first week. Over time the code base became unstable and painful. Facebook eventually changed its motto to "Move fast with solid infrastructure." Meanwhile, Google and VMware, founded around the same time, embraced strategic programming from the start and built sophisticated products with reliable systems.

## When Tactical Might Be Appropriate

- Extremely early prototypes where the code will be thrown away entirely
- Fixing a critical production incident where speed matters more than elegance (but the fix should be revisited strategically afterward)

Even in these cases, the tactical approach should be temporary and followed by strategic cleanup.

## When Strategic Is Essential

- Any codebase expected to be maintained for more than a few months
- Teams where multiple developers work on the same code
- Startups planning to scale — a tactical codebase makes it harder to recruit great engineers, who care about good design

Ousterhout's argument: the strategic approach is almost always better, and the payoff comes sooner than people think.

## Related
- [[strategic-programming]] — full concept page
- [[tactical-programming]] — full concept page
- [[design-investment]] — the 10–20% rule
- [[technical-debt]] — the compounding cost of tactical programming
- [[tactical-tornado]] — the extreme tactical archetype
- [[complexity]] — what both approaches have opposite relationships with
- [[a-philosophy-of-software-design-ch03]] — the chapter that develops this dichotomy
