---
title: Designing for Performance
aliases: [performance design, efficient design]
tags: [core-concept, performance, optimization]
sources: [a-philosophy-of-software-design, out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Designing for Performance

Designing for performance means achieving high performance without sacrificing clean design. Both [[a-philosophy-of-software-design|A Philosophy of Software Design]] and [[out-of-the-tar-pit|Out of the Tar Pit]] argue that simplicity and performance are allies, though they approach the relationship from different angles.

## In A Philosophy of Software Design

Designing for performance means achieving high performance without sacrificing clean design. The central insight is that simplicity and performance are allies, not enemies: simpler code tends to run faster because it does less extraneous or redundant work. [[deep-modules|Deep modules]] are naturally more efficient than shallow ones because they accomplish more per method call and avoid unnecessary layer crossings.

### The Middle Path

Two extremes are dangerous. Optimizing every statement adds [[complexity]] and slows development, while ignoring performance leads to "death by a thousand cuts" -- many small inefficiencies scattered throughout the codebase that collectively make the system 5-10x slower with no single fix available. The best approach is to develop awareness of fundamentally expensive operations (network I/O, disk I/O, dynamic memory allocation, cache misses) and choose naturally efficient alternatives when they are equally clean.

### Measure, Then Modify

Programmers' intuitions about performance are unreliable, even for experienced developers. Before optimizing, measure to identify where time is actually spent and establish a baseline. After changes, re-measure; if performance did not improve, back out the changes unless they simplified the code. There is no point retaining complexity unless it provides a significant speedup.

### Design Around the Critical Path

When specific code must be optimized, identify the "ideal" -- the minimum code that must execute in the common case, disregarding existing structure. Then redesign to approach that ideal while maintaining clean [[abstractions|abstractions]]. The key technique is removing special cases from the critical path: a single initial test should detect all special cases and branch away from the fast path. The RAMCloud Buffer class example demonstrated that this approach doubled performance while reducing code size by 20%.

### When to Add Complexity for Performance

If the only way to improve efficiency is by adding complexity, consider whether the complexity is hidden (safer) or exposed in interfaces (dangerous). If you have clear evidence that performance matters in a specific situation, implement the faster approach immediately. Otherwise, start simple and optimize later if needed.

## In Out of the Tar Pit

Moseley and Marks discuss performance in the context of [[state-and-complexity|accidental state]]. Caches, pre-computed data, and other performance-driven stored values are forms of accidental state — state that exists not because the problem demands it, but because we introduced it for speed. This accidental state is a major source of [[complexity]].

In their proposed Functional Relational Programming (FRP) architecture, performance concerns are isolated in dedicated "accidental" components. The essential logic — business rules and relations — remains pure and untainted by optimization concerns. "Performance hints" live in separate components that derive and cache results without polluting the essential specification.

The ideal is that performance should never drive the design of essential logic. Performance is treated as a separate concern, handled at a different architectural layer, rather than interleaved with business rules.

## Synthesis

Both argue that simplicity and performance are not enemies — they are natural allies. They agree on the principle but differ in mechanism.

Ousterhout shows that good design is naturally efficient: [[deep-modules|deep modules]] have less interface overhead, clean critical paths avoid wasted work, and simpler code has fewer unnecessary operations. His approach is to design well and then optimize measured bottlenecks, always keeping performance concerns within the existing module structure.

The Tar Pit shows that performance concerns can be architecturally isolated from essential logic. Rather than interleaving optimization with business rules, FRP separates them into distinct components. This is a more radical separation than Ousterhout proposes, but it shares his core insight: never let performance concerns drive your essential design.

Together they form a complete picture: Ousterhout's techniques work within any architecture to keep code clean and fast, while the Tar Pit's architectural separation prevents performance from ever corrupting the core logic. In practice, both insights apply — use clean design to avoid unnecessary inefficiency, and when optimization is needed, isolate it as much as possible from essential logic.

## Related
- [[complexity]] — simpler code tends to be faster
- [[deep-modules]] -- deep modules are naturally efficient
- [[abstractions]] -- performance optimization must preserve clean abstractions
- [[pull-complexity-downwards]] -- hiding complexity can also improve performance
- [[decide-what-matters]] -- deciding whether performance matters for a given module
- [[a-philosophy-of-software-design-ch20]] -- the source chapter
- [[designing-for-performance-vs-complexity]] — simplicity and performance as allies
- [[state-and-complexity]] — Tar Pit's analysis of how performance-driven state creates complexity
- [[accidental-complexity]] — performance optimizations as accidental complexity
- [[out-of-the-tar-pit]] — argues for isolating performance from essential logic
