---
title: "S2: Complexity"
tags: [complexity, simplicity]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# S2: Complexity

Of the four properties Brooks identified as making software hard -- Complexity, Conformity, Changeability, and Invisibility -- Moseley and Marks argue that only [[complexity]] is truly significant. The others are either forms of complexity or problematic solely because complexity already exists in the system. Complexity is the root cause of most software problems: unreliability, late delivery, lack of security, and poor performance in large-scale systems all trace back to unmanageable complexity.

The ability to understand a system is a prerequisite for avoiding all these problems, and complexity destroys that understanding. The authors cite a chorus of Turing Award winners making the same point across decades. Corbato warned that "the general problem with ambitious systems is complexity." Backus called for "a powerful methodology to help us think about programs" and noted that conventional languages create unnecessary confusion. Hoare observed that "the price of reliability is the pursuit of the utmost simplicity."

The paper draws an important distinction between the complexity it discusses -- which makes large systems hard to understand -- and computational complexity theory, which studies machine resources. A small program can be incredibly simple to understand yet belong to the highest complexity class in the theoretical sense. The two are completely unrelated.

The section ends with a sobering observation: "Simplicity is Hard." Achieving simplicity requires deliberate effort, and it is always easier to create a complicated solution first. The paper promises cause for optimism -- but only if we understand and attack the specific causes of complexity, which the following sections address.

This section resonates strongly with Ousterhout's treatment of [[complexity]] as the defining challenge of software, though Moseley and Marks focus more narrowly on state and control as causal mechanisms rather than on dependencies and obscurity.

Part of [[out-of-the-tar-pit]]

## Related
- [[complexity]] — central theme across both sources
- [[essential-vs-accidental-complexity]] — Brooks' distinction, refined
- [[out-of-the-tar-pit-s01]] — Introduction
- [[out-of-the-tar-pit-s03]] — Approaches to Understanding
- [[out-of-the-tar-pit-s04]] — Causes of Complexity
