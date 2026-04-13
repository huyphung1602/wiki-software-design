---
title: Temporal Decomposition
aliases: [time-based decomposition, execution-order decomposition]
tags: [anti-pattern, modules, design, red-flag]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Temporal Decomposition

Temporal decomposition is a design style where the structure of a system corresponds to the time order in which operations occur. It is a common cause of [[information-leakage]].

The classic example: an application that reads a file, modifies it, and writes it back. With temporal decomposition, this becomes three classes — a reader, a modifier, and a writer. Both reader and writer must understand the file format, creating information leakage. The solution: combine the core reading and writing mechanisms into a single class, used during both phases.

It's easy to fall into this trap because execution order is naturally on your mind when coding. But most design decisions manifest at several different times over an application's life. When order matters, it should be reflected somewhere — but not in the module structure unless that structure is consistent with [[information-hiding]].

**Red Flag: Temporal Decomposition** — If execution order is reflected in code structure and the same knowledge is used at different points, it gets encoded in multiple places, resulting in information leakage.

The HTTP server example illustrates this: one team split request handling into "read from network" and "parse the string" — but you can't read an HTTP request without parsing it (you need the Content-Length header to know the body length). Both classes ended up duplicating parsing knowledge.

The fix: design modules around **knowledge**, not **order**. Think about what information each task requires, and encapsulate related knowledge together.

## Cases
- [[kwic-index-two-decompositions]] — Decomposition 1 of the KWIC index exemplifies temporal decomposition: modules follow processing steps (Input → Circular Shift → Alphabetize → Output), and every change to shared data formats ripples through every module (from Criteria for Modularization)

## Related
- [[information-leakage]] — the direct result of temporal decomposition
- [[information-hiding]] — the principle it violates
- [[deep-modules]] — what temporal decomposition prevents
- [[red-flags]] — temporal decomposition as a recognized red flag
- [[a-philosophy-of-software-design-ch05]] — where this is named and analyzed
- [[problem-decomposition-vs-temporal-decomposition]] — comparison with the correct approach
