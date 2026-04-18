---
title: "Chapter 20 - Designing for Performance"
tags: [software-design, performance, optimization]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Chapter 20 - Designing for Performance

Part of [[a-philosophy-of-software-design]]

Clean design and high performance are compatible. The chapter's central insight is that [[designing-for-performance|simplicity usually makes systems faster]], because simpler code does less extraneous work. The key is to develop awareness of fundamentally expensive operations (network communication, disk I/O, dynamic memory allocation, cache misses) and choose naturally efficient alternatives when they are equally clean.

## How to Think About Performance

Two extremes are dangerous: optimizing every statement slows development and creates complexity, while ignoring performance entirely leads to "death by a thousand cuts" where many small inefficiencies make the system 5-10x slower with no single fix. The middle path: use knowledge of expensive operations to choose clean but efficient design alternatives. Micro-benchmarks are recommended for building this awareness.

## Measure Before Modifying

Programmers' intuitions about performance are unreliable, even for experienced developers. Before optimizing, measure to identify where time is actually spent and to establish a baseline. After making changes, re-measure; if performance did not improve, back out the changes unless they simplified the system.

## Design Around the Critical Path

When a specific piece of code must be optimized, identify the "ideal" -- the minimum code that must execute for the common case, ignoring existing structure. Then redesign to approach that ideal while maintaining clean [[abstractions|abstractions]]. The most important technique: remove special cases from the critical path. A single initial test should detect all special cases, branching off the critical path for them. The RAMCloud Buffer class example demonstrates this: refactoring around the critical path doubled performance while reducing code size by 20%.

## Related
- [[designing-for-performance]] -- the concept page for this chapter's core idea
- [[deep-modules]] -- deep modules are naturally more efficient than shallow ones
- [[abstractions]] -- performance optimization must preserve clean abstractions
- [[complexity]] -- simpler code tends to be faster code
- [[pull-complexity-downwards]] -- hiding complexity in implementations can also improve performance
