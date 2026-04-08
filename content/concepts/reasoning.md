---
title: Reasoning
aliases: [informal reasoning, code reasoning, white-box analysis, mental simulation]
tags: [core-concept, reasoning, software-quality, validation]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Reasoning

Informal reasoning is the approach to understanding a software system from the inside — by examining its code and constructing a mental model of its behavior. It is more important than [[testing]] because improvements in reasoning prevent errors from being created, while improvements in testing can only detect errors that already exist.

## In Out of the Tar Pit

Moseley and Marks argue that informal reasoning is "the most important by far" of the two approaches to understanding software. The justification is threefold: reasoning is always used (as an inherent part of development), improvements in reasoning prevent errors at the source, and reasoning can in principle cover the entire state space by working at the level of invariants rather than enumerating cases.

Reasoning typically involves case-by-case mental simulation: "if this variable is in this state, then this will happen — which is correct — otherwise that will happen." As the number of states grows, this approach buckles. [[State-and-complexity]] contaminates reasoning through "transitive statefulness" — a stateless procedure that calls a stateful one becomes contaminated and can only be understood in the context of state.

[[Referential-transparency]] makes reasoning far more effective. When a function depends only on its arguments, the developer can reason about it in isolation. Equational reasoning — substituting equals for equals — becomes possible. Each function becomes a local proof obligation rather than a piece of a global puzzle.

[[Control-flow-complexity]] also degrades reasoning by forcing the developer to determine whether the specified ordering is significant. In imperative languages, the programmer must start from the assumption that textual ordering matters, then determine by inspection that it doesn't — mistakes in this determination introduce subtle bugs.

The priority of reasoning over testing leads to a key design principle: invest in simplicity over testability. A simple system can be reasoned about effectively; a complex one cannot, regardless of how many tests are written.

## Related
- [[testing]] — the complementary but less powerful approach
- [[testing-vs-reasoning]] — why reasoning is prioritized and how complexity affects each differently
- [[referential-transparency]] — the property that makes reasoning effective
- [[complexity]] — the force that degrades reasoning ability
- [[cognitive-load]] — the mental capacity limit that constrains reasoning
- [[out-of-the-tar-pit-s03]] — where the argument for reasoning is developed
