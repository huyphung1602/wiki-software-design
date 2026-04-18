---
title: Out of the Tar Pit
tags:
  - complexity
  - state
  - functional-programming
  - relational-model
  - frp
sources:
  - out-of-the-tar-pit
created: 2026-04-08
updated: 2026-04-08
---

# Overview

**Authors:** Ben Moseley and Peter Marks
**Year:** 2006
**Venue:** Essays from the OOPSLA conference / Trends series

## Summary

Moseley and Marks argue that [[complexity]] is the single greatest problem in large-scale software systems, and that mutable [[state-and-complexity]] is its primary cause. Control flow and code volume are secondary contributors. Rather than managing complexity after it arises, the authors advocate two principles: **avoid** accidental complexity entirely, and **separate** essential complexity from everything else.

The paper proposes [[functional-relational-programming]] (FRP), a hypothetical architecture that combines pure functional programming with the [[relational-model]]. An FRP system is cleanly divided into essential state (base relations), essential logic (derived relations, pure functions, and declarative [[integrity-constraints]]), and accidental state and control (performance hints). Each component uses a different, restricted language. The separation ensures that accidental concerns can never contaminate essential logic, and that the system can never enter an inconsistent state due to logic errors.

The paper's central disagreement with Brooks is over whether complexity is essential or accidental. Where Brooks saw complexity as inherent in software, Moseley and Marks argue that most of the complexity we observe is accidental -- introduced by language choices, architectural decisions, and premature performance optimization. This is cause for optimism: if most complexity is accidental, it can be eliminated.

## Sections

1. [[out-of-the-tar-pit-s01]] -- Introduction: the software crisis and the proposal
2. [[out-of-the-tar-pit-s02]] -- Complexity: why it is the root cause
3. [[out-of-the-tar-pit-s03]] -- Approaches to Understanding: testing vs. informal reasoning
4. [[out-of-the-tar-pit-s04]] -- Causes of Complexity: state, control, code volume
5. [[out-of-the-tar-pit-s05]] -- Classical Approaches: OOP, functional, logic programming
6. [[out-of-the-tar-pit-s06]] -- Accidents and Essence: redefining the boundary
7. [[out-of-the-tar-pit-s07]] -- Recommended General Approach: avoid and separate
8. [[out-of-the-tar-pit-s08]] -- The Relational Model: structure, manipulation, integrity, data independence
9. [[out-of-the-tar-pit-s09]] -- Functional Relational Programming: the FRP architecture
10. [[out-of-the-tar-pit-s10]] -- Example of an FRP System: estate agency case study
11. [[out-of-the-tar-pit-s11]] -- Related Work
12. [[out-of-the-tar-pit-s12]] -- Conclusions: simplicity as the silver bullet

## Key Themes

- **Complexity elimination over management.** Where Ousterhout focuses on managing [[complexity]] through [[deep-modules]] and [[information-hiding]], Moseley and Marks argue for eliminating entire categories of complexity by avoiding mutable state and explicit control flow.
- **State as the primary enemy.** The paper identifies [[state-and-complexity]] as the single biggest cause of software difficulty, more impactful than code volume or architectural patterns.
- **Separation of concerns at the architecture level.** The three-way split (essential state, essential logic, accidental) goes deeper than [[modular-design]] by restricting the expressive power of each component's language.
- **Declarative over imperative.** [[declarative-programming]] is not merely preferred but required: integrity constraints, derived relations, and performance hints are all specified declaratively.
- **The accidental/essential distinction.** [[essential-vs-accidental-complexity]] is applied more rigorously than in Brooks' original formulation, with "essential" meaning only what the users' problem requires.

## Cross-References with A Philosophy of Software Design

Both papers treat [[complexity]] as the central problem, but they approach it differently:

- **Ousterhout** focuses on managing complexity through module design ([[deep-modules]], [[information-hiding]], [[abstractions]]). His remedies are practical and applicable to any codebase.
- **Moseley and Marks** focus on eliminating complexity by changing fundamental architectural choices (avoiding state, separating concerns). Their remedies are more radical but harder to adopt incrementally.

Both agree on the dangers of premature optimization ([[designing-for-performance]]), the importance of [[strategic-programming]] over [[tactical-programming]], and the principle that simplicity must be actively pursued. Where Ousterhout says "the most important thing is to make the interface simple," Moseley and Marks say "the most important thing is to make the system stateless and declarative."

## Related
- [[complexity]] -- central theme across both sources
- [[state-and-complexity]] -- the primary cause identified in this paper
- [[essential-vs-accidental-complexity]] -- the refined Brooks distinction
- [[functional-relational-programming]] -- the proposed architecture
- [[referential-transparency]] -- the key property of pure functional components
- [[relational-model]] -- the data foundation of FRP
- [[declarative-programming]] -- the paradigm underlying FRP
- [[designing-for-performance]] -- both papers warn against premature optimization
- [[strategic-programming]] -- investing in design for long-term system health
