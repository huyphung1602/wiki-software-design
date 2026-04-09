---
title: Control Flow Complexity
aliases: [control complexity, flow of control, unnecessary ordering]
tags: [core-concept, complexity, control-flow, software-design]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Control Flow Complexity

Explicit concern with the flow of control through a system is a major source of [[complexity]]. Moseley and Marks identify control flow as the second most important cause of complexity after [[state-and-complexity|state]]. The core problem is that control flow forces developers to specify ordering — this must happen before that — even when the problem domain imposes no such constraint.

## The Problem with Ordering

When a specification says "compute A, then compute B, then compute C," it introduces an ordering constraint that may be entirely accidental. If B does not depend on A, and C does not depend on either, the sequential specification adds complexity without adding value. The developer must understand and maintain an order that has no logical basis.

[[temporal-decomposition]] is a common manifestation of this problem. Systems designed around a sequence of operations — do step 1, then step 2, then step 3 — embed control flow into their architecture. When requirements change and the ordering must shift, the system resists modification because the ordering is woven throughout the code.

## Control Flow as Accidental Complexity

In Moseley and Marks' framework, most control flow is [[accidental-complexity|accidental complexity]]. The problem domain rarely specifies that things must happen in a particular order — it specifies what must be true when the system is done. The ordering is an implementation detail, not a requirement. [[declarative-programming]] eliminates this by specifying what should be computed, not the sequence in which computations occur.

In an ideal system, control flow would be entirely accidental and managed automatically. Database query engines already demonstrate this: SQL specifies what data to retrieve, and the engine determines the optimal execution plan. The programmer never specifies whether to scan or use an index, whether to join or filter first.

## Relation to State

Control flow and state interact destructively. When code must execute in a specific order because earlier steps modify state that later steps depend on, the result is a tightly coupled system where changes cascade unpredictably. Eliminating state through [[referential-transparency]] also eliminates many control flow dependencies, because pure functions can be executed in any order.

## Related
- [[state-and-complexity]] — the primary cause of complexity, intertwined with control flow
- [[complexity]] — the overarching problem
- [[declarative-programming]] — the paradigm that eliminates control flow complexity
- [[temporal-decomposition]] — a design anti-pattern driven by control flow concerns
- [[functional-relational-programming]] — an architecture that minimizes explicit control flow
- [[accidental-complexity]] — most control flow is accidental
