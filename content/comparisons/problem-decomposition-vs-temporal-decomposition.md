---
title: Problem Decomposition vs Temporal Decomposition
aliases: [temporal decomposition vs problem decomposition, knowledge-based vs time-based decomposition]
tags: [comparison, design, decomposition, modules]
sources: [a-philosophy-of-software-design, criteria-for-modularization]
created: 2026-04-08
updated: 2026-04-13
---

# Problem Decomposition vs Temporal Decomposition

The most fundamental design decision: how to divide a system into modules. One approach follows knowledge boundaries. The other follows execution order. They produce radically different systems.

## Problem Decomposition: organize around knowledge

Divide the system into modules where each encapsulates a distinct piece of knowledge — a design decision that could change independently. The criteria come from David Parnas (1972): modules should hide information from each other, and the decomposition should minimize the knowledge any module needs about others. This produces [[deep-modules]] with strong [[information-hiding]]. See [[problem-decomposition]] for the full concept.

### Evidence from Criteria for Modularization

Parnas's KWIC index case study makes this concrete. Decomposition 1 (Input → Circular Shift → Alphabetize → Output) is temporal/processing-based. Decomposition 2 (Line Storage, Circular Shifter, Alphabetizer) is knowledge-based. Five hypothetical changes were tested against both. In Decomposition 1, four of five changes propagate to every module because shared data formats and storage decisions are visible across all processing-step modules. In Decomposition 2, each change stays isolated — the design decision is hidden within the module that owns it. The same running code, the same functional result, completely different maintenance properties. This is the most cited evidence for why problem decomposition (information hiding) should replace temporal decomposition as the default criterion.

## Temporal Decomposition: organize around execution order

Structure the system to match the sequence of operations: read, then parse, then process, then write. It feels natural because execution order is what you think about when coding. But most design decisions manifest at several different times over an application's life, so splitting by time spreads knowledge across modules. See [[temporal-decomposition]] for the full concept.

## The Tension

Both approaches decompose a system — the question is *what axis* to cut along.

| Aspect | Problem Decomposition | Temporal Decomposition |
|--------|----------------------|----------------------|
| Cutting axis | Knowledge boundaries | Execution order |
| Module cohesion | High — related knowledge together | Low — knowledge spread across phases |
| Information hiding | Strong — each module owns its knowledge | Weak — shared knowledge leaks across phases |
| Change impact | Localized — change affects one module | Amplified — change ripples across phases |
| Natural feel | Requires deliberate design | Feels natural during coding |
| Example | File class that handles both reading and writing | Separate reader class and writer class |

The HTTP server example illustrates the trap: splitting "read from network" from "parse the string" seems logical — they happen at different times. But you can't read an HTTP request without parsing it (the Content-Length header tells you the body size). Both classes ended up duplicating parsing knowledge. The fix: a single class that understands HTTP request structure, used during both reading and parsing.

The file format example: temporal decomposition creates a reader, a modifier, and a writer. Both reader and writer must understand the file format. Problem decomposition creates a single class that encapsulates the file format, handling both reading and writing.

## When Problem Decomposition Is the Right Choice

- Always. This should be the default approach to system design.
- When modules need to evolve independently.
- When implementation details are likely to change.

## When Temporal Patterns Are Acceptable

- At the highest levels of an application, where execution phases (initialize, process, cleanup) are reflected in orchestration code — not in module boundaries.
- When the phases genuinely share no knowledge (reading from one format and writing to a completely different one).
- When used as a *guide*, not a *rule* — execution order can suggest where to look for knowledge boundaries, but the final decomposition should follow knowledge.

The key test: if changing a design decision requires modifying multiple modules, the decomposition is wrong. Reorganize around knowledge.

## Cases
- [[kwic-index-two-decompositions]] — KWIC index's two decompositions are the primary example; Decomposition 1 is temporal (processing steps), Decomposition 2 is knowledge-based (design decisions), with five-change test showing how the decomposition criterion controls change propagation (from Criteria for Modularization)

## Related
- [[problem-decomposition]] — full concept page
- [[temporal-decomposition]] — full concept page
- [[information-hiding]] — the goal of problem decomposition
- [[information-leakage]] — the result of temporal decomposition
- [[deep-modules]] — what problem decomposition produces
- [[a-philosophy-of-software-design-ch05]] — where temporal decomposition is named and analyzed
