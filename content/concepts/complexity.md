---
title: Complexity
aliases: [software complexity, system complexity]
tags: [core-concept, complexity, software-design]
sources: [a-philosophy-of-software-design, out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Complexity

Complexity is widely recognized as the central problem in software design. Both [[a-philosophy-of-software-design|A Philosophy of Software Design]] and [[out-of-the-tar-pit|Out of the Tar Pit]] treat complexity as the root cause of software failures, though they analyze its causes and remedies differently.

## In A Philosophy of Software Design

Complexity is the overarching enemy in software design. Ousterhout argues that the primary goal of software design is to reduce complexity — this matters more than adherence to any particular principle or technique.

Complexity accumulates incrementally as a system grows. It manifests as subtle dependencies between components, making it harder for programmers to understand and modify the system. Left unchecked, complexity makes development progressively slower and more error-prone.

The book treats complexity as the central problem that all its design principles address: [[deep-modules]], [[information-hiding]], [[strategic-programming]], [[choosing-names|consistent naming]], and so on are all ultimately in service of reducing complexity. Deep modules are the primary structural tool — they hide the maximum complexity behind the minimum interface. [[Shallow-modules]] and [[classitis]] are anti-patterns because they add interface complexity without hiding proportionally more implementation complexity.

## In Out of the Tar Pit

Moseley and Marks argue that complexity is the single root cause of all software problems — unreliability, late delivery, lack of security, and poor performance all trace back to complexity. They identify [[state-and-complexity|state]] as the single biggest cause of complexity, followed by [[control-flow-complexity|control flow]] and [[cognitive-load|code volume]].

The paper draws the classic distinction between [[essential-vs-accidental-complexity|essential and accidental complexity]], originally from Fred Brooks, but disagrees with Brooks's pessimism that most complexity is essential. Moseley and Marks argue that much of what we consider essential complexity is actually accidental — introduced by our choice of tools and architectures rather than inherent in the problem. They cite Dijkstra, Hoare, and Corbato on the paramount importance of simplicity.

Their thesis is that by choosing fundamentally simpler architectures (such as Functional Relational Programming), we can eliminate large categories of accidental complexity rather than merely managing them.

## Synthesis

Both identify complexity as the central problem in software. Their analyses are complementary but differ in depth and prescription.

Ousterhout focuses on **symptoms** ([[change-amplification|change amplification]], [[cognitive-load|cognitive load]], [[unknown-unknowns|unknown unknowns]]) and **structural causes** (dependencies, obscurity). His remedy is to manage complexity through design: deep modules, information hiding, and strategic investment.

Moseley and Marks focus on **deeper causes** ([[state-and-complexity|state]], [[control-flow-complexity|control flow]], [[cognitive-load|code volume]]) and argue that most complexity is accidental rather than essential. Their remedy is to eliminate complexity by avoiding state and mutable control flow entirely, through architectures like FRP.

These perspectives are complementary — Ousterhout gives practical techniques for the world we have (managing complexity through good design), while the Tar Pit points toward a more radical architecture that could eliminate entire categories of complexity. A practitioner can benefit from both: use Ousterhout's techniques day-to-day while keeping the Tar Pit's vision as a north star for architectural decisions.

## Related
- [[problem-decomposition]] — the primary tool for managing complexity
- [[strategic-programming]] — investing in design to prevent complexity from accumulating
- [[deep-modules]] — the primary structural tool for hiding complexity
- [[shallow-modules]] — modules that add complexity without compensating benefit
- [[modular-design]] — the framework for encapsulating complexity
- [[a-philosophy-of-software-design]] — the book that places complexity reduction at its core
- [[designing-for-performance-vs-complexity]] — simplicity and performance as allies
- [[state-and-complexity]] — Tar Pit's analysis of state as the primary cause of complexity
- [[essential-vs-accidental-complexity]] — the distinction between inherent and introduced complexity
- [[out-of-the-tar-pit]] — the paper that argues most complexity is accidental
- [[out-of-the-tar-pit-s02]] — Tar Pit's sources of complexity
