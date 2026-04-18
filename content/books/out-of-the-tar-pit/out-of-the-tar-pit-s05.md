---
title: "S5: Classical Approaches to Managing Complexity"
tags: [oop, functional-programming, logic-programming, state, control-flow]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# S5: Classical Approaches to Managing Complexity

This section evaluates the three major programming paradigms through the lens of state and control.

**Object-Oriented Programming.** OOP encapsulates state within objects and regulates access through methods, but several fundamental problems remain. Encapsulation-based integrity enforcement is biased toward single-object constraints -- enforcing multi-object constraints is awkward. Object identity, intrinsic to OOP, creates a tension between intensional identity (objects are distinct regardless of attributes) and extensional identity (objects are the same if their attributes match). Developers must mentally switch between these two concepts, leading to confusion and errors. Fundamentally, OOP relies on state and all behavior is affected by it, so it suffers directly from all state-related problems.

**Functional Programming.** Pure functional programming avoids state entirely and gains [[referential-transparency]]: a function always returns the same result for the same arguments. This property dramatically improves both testing and reasoning. However, when real systems require state, functional programs must simulate it by threading extra parameters through every function. In extreme cases this recreates a pool of global variables, losing the reasoning benefits. Monads (as in Haskell) offer a middle path but can be abused to reintroduce all the problems being avoided. The trade-off is between complexity with shortcut convenience and simplicity with up-front discipline.

**Logic Programming.** Pure logic programming specifies what must be true rather than how to achieve it, promising escape from control complexity. In practice, languages like Prolog impose operational ordering (left-to-right, top-down) that requires concern with control flow. Extra-logical features like "cuts" further entangle control with logic. Despite these limitations, the paradigm shows that control can be separated from logic.

Each paradigm offers partial solutions but none adequately addresses both state and control simultaneously. This motivates the authors' search for a combined approach.

Part of [[out-of-the-tar-pit]]

## Related
- [[referential-transparency]] — the key property pure functional programming provides
- [[state-and-complexity]] — the problem all three paradigms wrestle with
- [[control-flow-complexity]] — the problem logic programming partially solves
- [[out-of-the-tar-pit-s04]] — Causes of Complexity
- [[out-of-the-tar-pit-s06]] — Accidents and Essence
