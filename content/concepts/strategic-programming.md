---
title: Strategic Programming
aliases: [strategic approach, investment mindset]
tags: [core-concept, programming-approach, investment]
sources: [a-philosophy-of-software-design, out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Strategic Programming

Strategic programming is the practice of investing in design quality upfront rather than racing to finish the current task. Both [[a-philosophy-of-software-design|A Philosophy of Software Design]] and [[out-of-the-tar-pit|Out of the Tar Pit]] advocate for this mindset, though they differ in how radical the investment should be.

## In A Philosophy of Software Design

Strategic programming is an investment mindset: the primary goal is to produce a great design, which also happens to work. Rather than taking the fastest path to finish the current task, you invest time to improve the design of the system. These investments slow you down in the short term but speed you up in the long term as [[complexity]] grows more slowly.

Strategic investments are both **proactive** and **reactive**. Proactive investments include finding simpler designs before implementing, considering alternative approaches, and writing good documentation. Reactive investments happen when you discover design problems — instead of patching around them, you take time to fix the underlying issue.

The rule of thumb: spend [[design-investment|10–20% of total development time]] on design investments. This is small enough not to impact schedules significantly but large enough to produce compounding benefits. Initial projects take 10–20% longer, but within 6–18 months the benefits from past investments cover the cost of future ones. After that, strategic programming is effectively free.

The opposite approach is [[tactical-programming]], which feels productive in the short term but accumulates complexity relentlessly. The accumulated cost is [[technical-debt]] — and unlike financial debt, most tech debt is never fully repaid.

It's crucial to be consistent: when you get in a crunch, it's tempting to put off cleanups until after. But this is a slippery slope — after the current crunch there will almost certainly be another. The longer you wait to address design problems, the bigger they become and the easier it is to keep putting them off. See [[strategic-vs-tactical-programming]] for the full comparison.

## In Out of the Tar Pit

Moseley and Marks argue for a strategic approach to [[complexity]] from a different angle: invest in simplicity upfront by choosing architectures that eliminate [[accidental-complexity|accidental complexity]] rather than just managing it. They quote Hoare: "The price of reliability is the pursuit of the utmost simplicity."

Where Ousterhout advocates incremental design improvement within conventional architectures, the Tar Pit argues for a more fundamental strategic choice: selecting architectures (like Functional Relational Programming) that remove entire categories of complexity by construction. The ideal is not to manage complexity through good design, but to avoid it entirely through architectural choices that make certain kinds of complexity impossible.

This aligns with Ousterhout's strategic programming in spirit — both say "invest now to save later" — but differs in the scale and nature of the investment. The Tar Pit's version is less about continuous refactoring and more about getting the architectural foundation right from the start.

## Synthesis

Both advocate for upfront investment in design quality over short-term speed. They agree on the direction but differ in degree and mechanism.

Ousterhout's approach is **incremental and practical**: invest 10–20% of development time in continuous design improvement, refactoring as you go, and accepting that complexity management is an ongoing discipline. This works within any architecture.

The Tar Pit's approach is **radical and architectural**: choose fundamentally simpler architectures upfront so that entire categories of complexity never arise. The investment is larger and more front-loaded, but the payoff is eliminating (not just managing) complexity.

These are not contradictory. A practitioner can adopt Ousterhout's 10–20% investment habit for day-to-day work while also making the Tar Pit's larger architectural bets when the opportunity arises — for example, choosing a simpler data model or eliminating mutable state in a new service. The combination yields both immediate improvement and long-term architectural clarity.

## Related
- [[tactical-programming]] — the opposite approach
- [[strategic-vs-tactical-programming]] — comparison of both approaches
- [[design-investment]] — the 10–20% rule
- [[technical-debt]] — the cost of tactical programming
- [[tactical-tornado]] — the extreme tactical archetype
- [[complexity]] — what strategic programming keeps under control
- [[continuous-design]] — design as an ongoing process
- [[a-philosophy-of-software-design-ch03]] — the chapter that develops this in full
- [[a-philosophy-of-software-design-ch16]] — strategic mindset when modifying existing code
- [[out-of-the-tar-pit]] — argues for strategic investment in simpler architectures
- [[essential-vs-accidental-complexity]] — Tar Pit's distinction that motivates radical simplification
- [[state-and-complexity]] — one of the key complexity sources to eliminate strategically
