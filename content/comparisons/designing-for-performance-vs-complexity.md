---
title: Designing for Performance vs Complexity
aliases: [complexity vs performance, simplicity vs speed, performance vs simplicity]
tags: [comparison, performance, complexity, design]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Designing for Performance vs Complexity

A widespread assumption: fast code must be complex, and simple code must be slow. Ousterhout argues the opposite — simplicity and performance are allies. This comparison explores when they reinforce each other and when genuine trade-offs emerge.

## Designing for Performance: fast without sacrificing design

Achieve high performance by developing awareness of expensive operations (network I/O, disk I/O, memory allocation, cache misses) and choosing naturally efficient alternatives when they are equally clean. Measure before optimizing. Design around the critical path. See [[designing-for-performance]] for the full concept.

## Complexity: the enemy that slows everything down

Complexity makes code harder to understand and modify. It accumulates incrementally and makes development progressively slower. The book's entire framework exists to reduce complexity. See [[complexity]] for the full concept.

## The Tension

The common belief is that performance and simplicity trade off against each other. The reality is more nuanced:

| Aspect | Conventional Wisdom | Ousterhout's View |
|--------|-------------------|-------------------|
| Relationship | Trade-off — one costs the other | Allies — simpler code tends to be faster |
| Deep modules | More layers = slower | Deep modules are naturally efficient (fewer layer crossings) |
| Special cases | Needed for edge case performance | Eliminating special cases simplifies AND speeds up the common path |
| Optimization | Add complexity to gain speed | Start simple, measure, optimize only where it matters |

Why simplicity helps performance:
- [[deep-modules|Deep modules]] accomplish more per method call and avoid unnecessary layer crossings
- Eliminating special cases removes branches from the critical path
- Simpler code does less extraneous or redundant work
- The RAMCloud Buffer example: redesigning for the critical path doubled performance while reducing code size by 20%

When genuine trade-offs emerge:
- Caching adds complexity but can dramatically improve performance
- Bit-packing and compression are inherently complex but save bandwidth
- Concurrent data structures are more complex than sequential ones

The rule: if the only way to improve performance is to add [[complexity]], ask:
1. Is the complexity hidden (safer) or exposed in interfaces (dangerous)?
2. Do you have clear evidence that performance matters in this specific situation?
3. Did you measure before and after?

## When to Favor Simplicity

- When measurement shows performance is adequate
- When the performance-critical path is unclear
- For most application-level code
- When the "optimization" adds exposed complexity (interface changes)

## When to Accept Complexity for Performance

- When measurement identifies a clear bottleneck
- When the complexity can be hidden behind a clean interface
- For infrastructure code used pervasively (network stacks, memory allocators, file systems)
- When a small, isolated performance optimization has outsized impact

The key insight: design for performance *from the start* by choosing naturally efficient approaches, but don't add complexity preemptively. Measure, then optimize where it matters.

## Related
- [[designing-for-performance]] — full concept page
- [[complexity]] — full concept page
- [[deep-modules]] — naturally efficient
- [[abstractions]] — performance optimization must preserve clean abstractions
- [[pull-complexity-downwards]] — hiding complexity can also improve performance
- [[a-philosophy-of-software-design-ch20]] — the source chapter on performance
