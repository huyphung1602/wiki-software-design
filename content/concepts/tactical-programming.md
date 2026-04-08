---
title: Tactical Programming
aliases: [tactical approach, short-term thinking, move fast and break things]
tags: [anti-pattern, programming-approach, complexity]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Tactical Programming

Tactical programming is a short-sighted approach where the main focus is getting something working as quickly as possible — a new feature, a bug fix, a deadline. Planning for the future isn't a priority. You don't spend time looking for the best design; you just want to get something working soon. Each quick fix adds a bit of [[complexity]], and you tell yourself it's OK if it allows the current task to be completed faster.

This is how systems become complicated. Complexity is incremental — it's not one particular thing but the accumulation of dozens or hundreds of small compromises. If you program tactically, each task contributes a few of these complexities, and they accumulate rapidly, especially if everyone is programming tactically.

Before long, the complexities start causing problems. But you tell yourself it's more important to get the next feature working than to refactor. So you look for quick patches to work around problems, which creates more complexity, which requires more patches. Pretty soon the code is a mess, but by then it would take months to clean up. See [[strategic-vs-tactical-programming]] for the full comparison.

The extreme tactical programmer is the [[tactical-tornado]] — a prolific programmer who pumps out code far faster than others but leaves behind a wake of destruction. Other engineers must clean up the messes, which makes it appear that those engineers are making slower progress.

## Related
- [[strategic-programming]] — the opposite approach
- [[strategic-vs-tactical-programming]] — comparison of both approaches
- [[tactical-tornado]] — the extreme tactical archetype
- [[technical-debt]] — the cost of tactical programming
- [[complexity]] — what tactical programming accumulates
- [[a-philosophy-of-software-design-ch03]] — the chapter that develops this in full
