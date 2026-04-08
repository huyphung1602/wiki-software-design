---
title: Accidental Complexity
aliases: [incidental complexity, implementation complexity, unnecessary complexity, accidental difficulty]
tags: [core-concept, complexity, software-design, philosophy]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Accidental Complexity

Accidental complexity is all complexity that is not inherent in the users' problem — complexity that the development team would not have to deal with in an ideal world. It arises from performance concerns, suboptimal languages, infrastructure limitations, and — most critically — from architectural choices that introduce unnecessary [[state-and-complexity|state]], [[control-flow-complexity|control flow]], and code volume.

## In Out of the Tar Pit

Moseley and Marks disagree forcefully with Brooks, who argued that most accidental complexity had already been eliminated by high-level languages and that remaining complexity was largely essential. They contend that most complexity in contemporary systems is still accidental — introduced by mutable state, explicit control flow ordering, and code that manages both.

The three primary sources of accidental complexity are:
- **Mutable state**: the single biggest cause. Each bit of mutable state doubles the number of possible configurations, creating an exponential explosion that makes testing and reasoning infeasible.
- **Explicit control flow**: forcing developers to specify the order of operations when the problem domain often doesn't care about order. The programmer is forced to over-specify.
- **Code volume**: much code exists solely to manage state and control flow. Reducing these sources automatically reduces code volume.

If most complexity is accidental, then significant simplification is achievable through better architectural choices. [[Functional-relational-programming]] aims to eliminate accidental complexity by separating essential state (stored as relations), essential logic (expressed as pure functions and relational algebra), and accidental concerns (isolated in a separate component). The system should still function correctly if all accidental components are removed — just more slowly.

Accidental state specifically includes caches, memoized results, precomputed aggregations, and any derived data that could be re-derived from essential state on demand. In the ideal world, none of this would be stored.

## Related
- [[essential-complexity]] — the counterpart: complexity that cannot be eliminated
- [[essential-vs-accidental-complexity]] — the distinction and how to classify complexity
- [[state-and-complexity]] — the primary source of accidental complexity
- [[control-flow-complexity]] — the second major source
- [[accidental-state]] — state that can be eliminated
- [[technical-debt]] — accumulated accidental complexity viewed as debt
- [[functional-relational-programming]] — architecture that minimizes accidental complexity
- [[out-of-the-tar-pit-s06]] — where the classification is developed
