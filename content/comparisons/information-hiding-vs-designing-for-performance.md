---
title: Information Hiding vs Designing for Performance
aliases: [hiding vs performance, performance cost of abstraction, abstraction overhead]
tags: [comparison, modules, performance, information-hiding]
sources: [a-philosophy-of-software-design, criteria-for-modularization]
created: 2026-04-13
updated: 2026-04-13
---

# Information Hiding vs Designing for Performance

Information hiding and performance are natural allies in well-designed systems, but Parnas identified a tension: the abstraction mechanism itself (procedure calls between modules) can impose a runtime cost. This comparison examines when the two reinforce each other and when they conflict.

## Information Hiding (from A Philosophy of Software Design and Criteria for Modularization)

Information hiding — each module encapsulates design decisions, keeping them invisible to other modules — is the primary technique for achieving [[deep-modules]]. It reduces [[change-amplification]], simplifies interfaces, and enables independent evolution. Ousterhout argues that [[deep-modules|deep modules]] are naturally efficient because they do more per call and avoid unnecessary layer crossings. See [[information-hiding]] for the full concept.

## Designing for Performance (from A Philosophy of Software Design)

Designing for performance means achieving high performance without sacrificing clean design. The central insight is that simplicity and performance are allies: simpler code tends to be faster because it does less extraneous or redundant work. Deep modules are naturally efficient. See [[designing-for-performance]] for the full concept.

## The Tension

The conventional wisdom holds that hiding information behind clean interfaces has no runtime cost — the abstraction is purely a development-time concern. Parnas challenges this directly.

In Parnas's KWIC index example, Decomposition 2 (information hiding) is the superior decomposition for changeability and independent development. But if each function in Decomposition 2 is implemented as a procedure with an elaborate calling sequence, there will be frequent module-switching overhead. Decomposition 1 (processing steps) does not have this problem because there are relatively few cross-module calls. The information-hiding decomposition is potentially less efficient purely because of the interface structure.

Parnas's proposed solution is characteristically blunt: implement modules by injecting code directly (via assembler) rather than through conventional subroutine calls. This preserves the abstraction while recovering performance — but it adds tooling complexity and obscures the module boundaries in the final code.

Ousterhout's position is different. He argues that deep modules are naturally efficient because they minimize layer crossings. But this assumes the abstraction mechanism itself (method calls) is cheap. Parnas shows that when every module call traverses a clean interface boundary, the overhead accumulates.

## When They Align

When information hiding produces [[deep-modules]] — simple interfaces backed by rich implementations — the two reinforce each other. The interface is narrow, so call overhead is low. The implementation is rich, so each call does significant work. A B-tree class with a simple `find(key)` interface is information hiding AND high performance; the abstraction costs nothing at runtime.

## When They Conflict

When information hiding is applied at a fine grain — every design decision behind its own interface boundary, with frequent cross-module calls — the abstraction overhead can dominate. Parnas's point is not that information hiding is wrong, but that implementing it naively (as procedure calls) has a real cost, and recovering that cost requires departing from the conventional subroutine model.

The key question: does this module boundary reflect a significant design decision worth insulating, or does it create unnecessary call overhead? Deep modules solve this by making each interface narrow enough that the overhead is negligible — the call does enough work to justify the crossing.

## Synthesis

Parnas and Ousterhout agree that clean design and performance are compatible, but they arrive at this conclusion differently. Ousterhout argues that good design IS naturally efficient (deep modules, clean critical paths). Parnas shows that this only holds if you implement the abstractions efficiently — and that implementing information hiding naively (via subroutine calls) can hurt performance. The resolution: the abstraction must be preserved in the development representation, but the implementation representation can map across module boundaries to recover performance. This requires multiple program representations maintained together — a tooling burden that Parnas acknowledges.

## Related
- [[information-hiding]] — the technique whose performance cost is examined
- [[designing-for-performance]] — the goal and the approach
- [[deep-modules]] — where hiding and performance align (narrow interface, rich implementation)
- [[criteria-for-modularization-ch01]] — Parnas's performance analysis section
- [[designing-for-performance-vs-complexity]] — the general simplicity-vs-speed comparison