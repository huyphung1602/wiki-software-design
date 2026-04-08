---
title: Deep Modules vs Shallow Modules
aliases: [shallow modules vs deep modules, depth vs shallowness]
tags: [comparison, modules, design, encapsulation]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Deep Modules vs Shallow Modules

The fundamental measure of a module's value: does its interface complexity justify the functionality it provides? Deep modules deliver maximum benefit at minimum cost. Shallow modules do the opposite — they add interface complexity without hiding proportionally more implementation complexity.

## Deep Modules: simple interface, powerful functionality

A deep module provides powerful functionality through a simple interface. The canonical example is Unix file I/O: five system calls with simple signatures, backed by hundreds of thousands of lines of implementation. A garbage collector is even deeper — it has no interface at all, yet hides enormous complexity. Depth is achieved through [[information-hiding]] and [[generality|general-purpose interfaces]]. See [[deep-modules]] for the full concept.

## Shallow Modules: complex interface, trivial functionality

A shallow module's interface is relatively complex compared to what it provides. Linked lists are a typical example — inserting or deleting takes a few lines of code, so the abstraction hides almost nothing. The extreme case is a wrapper method that just calls one other method, offering no abstraction while adding a new interface to learn. [[classitis]] and [[information-leakage]] are common causes. See [[shallow-modules]] for the full concept.

## The Tension

The "depth" metaphor makes this a cost-benefit calculation. Imagine modules as rectangles: the top edge is the interface (cost), the area is the functionality (benefit).

| Aspect | Deep Modules | Shallow Modules |
|--------|-------------|-----------------|
| Interface complexity | Low | High relative to functionality |
| Implementation complexity | High (but hidden) | Low (not much to hide) |
| Cognitive load on users | Low — learn a few simple methods | High — learn many methods, each trivial |
| Change amplification | Low — internals change freely | High — changes ripple through callers |
| Information hiding | Excellent | Poor to none |
| Example | Unix file I/O, garbage collector | Linked list wrapper, getters/setters |

The trap: small modules *feel* clean and focused. But [[classitis]] — the cultural bias toward many small classes — produces systems full of shallow modules with enormous collective interface complexity. The Unix I/O API would be far worse if split into separate modules for disk layout, permissions, caching, and device abstraction.

## When Deep Modules Are the Right Choice

- Almost always. Depth should be the default goal.
- For any module that will be used by multiple callers or maintained over time.
- When implementation details are likely to change (depth insulates callers from change).

## When Shallow Modules Might Be Acceptable

- Modules with unavoidably simple implementations (like linked lists) — they can still be useful, just don't expect them to manage complexity.
- Performance-critical data structures where the overhead of abstraction isn't justified.
- Boundary cases where the interface is genuinely simple even if the implementation is trivial.

The key question: is this module paying its way? If its interface complexity is not offset by the complexity it hides, it's making the system worse.

## Related
- [[deep-modules]] — full concept page
- [[shallow-modules]] — full concept page
- [[information-hiding]] — the primary technique for achieving depth
- [[information-leakage]] — prevents depth
- [[classitis]] — the cultural pattern that produces many shallow modules
- [[complexity]] — what deep modules manage and shallow modules fail to manage
- [[a-philosophy-of-software-design-ch04]] — where depth is defined
