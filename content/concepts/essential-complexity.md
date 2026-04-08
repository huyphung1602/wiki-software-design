---
title: Essential Complexity
aliases: [inherent complexity, problem-domain complexity, essential difficulty]
tags: [core-concept, complexity, software-design, philosophy]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Essential Complexity

Essential complexity is complexity inherent in the problem as seen by the users. It cannot be avoided — only managed. Even in an ideal world with perfect languages and infrastructure, a development team would still have to contend with it.

## In Out of the Tar Pit

Moseley and Marks refine Brooks' original definition with a stricter criterion: something is essential only if it is inherent in, and the essence of, the problem as seen by the users. This is deliberately more restrictive than common usage — bits, bytes, transistors, electricity, and even computers themselves are not essential, because they have nothing to do with the users' problem.

The test for essential complexity is: could the team produce a system users consider correct without being concerned with this complexity? If yes, it is not essential. The "have to" part is critical — if there is any possible way to avoid a type of complexity while still solving the users' problem, that complexity is not essential.

In the ideal world, essential complexity consists of:
- **Essential state**: data that users directly input and that the system must retain for future reference
- **Essential logic**: the business rules, constraints, and derived relationships that define correct behavior

Even [[functional-relational-programming]], which aggressively eliminates [[accidental-complexity]], retains essential state as relations and essential logic as derived-relation definitions and [[integrity-constraints]]. The goal is not to eliminate essential complexity, but to isolate it from everything else.

## Related
- [[accidental-complexity]] — the counterpart: complexity that can be eliminated
- [[essential-vs-accidental-complexity]] — the distinction and its practical implications
- [[complexity]] — the overarching problem
- [[functional-relational-programming]] — an architecture that isolates essential complexity
- [[out-of-the-tar-pit-s06]] — where the refined definition is developed
