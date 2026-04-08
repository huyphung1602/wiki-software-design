---
title: Information Hiding vs Information Leakage
aliases: [information leakage vs information hiding, encapsulation vs leakage, hiding vs leaking]
tags: [comparison, modules, design, encapsulation]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Information Hiding vs Information Leakage

Two opposing forces in module design: encapsulating knowledge within a single module, or allowing it to spread across multiple modules. The quality of a system's design depends largely on which force dominates.

## Information Hiding: encapsulate knowledge

Each module encapsulates a few design decisions in its implementation, keeping them invisible to other modules. Hidden knowledge includes data structures, algorithms, and assumptions. This produces [[deep-modules]] — simple interfaces backed by complex, changeable implementations. See [[information-hiding]] for the full concept.

## Information Leakage: spread knowledge

A design decision is reflected in multiple modules, creating a dependency — any change to that decision requires changes to all involved modules. Leakage can happen through interfaces (exposing internal representations) or "back-door" through shared knowledge (two classes both understanding a file format). See [[information-leakage]] for the full concept.

## The Tension

Every design decision in a system must live somewhere. The question is: how many modules know about it?

| Aspect | Information Hiding | Information Leakage |
|--------|-------------------|-------------------|
| Knowledge location | One module | Multiple modules |
| Change impact | One module changes | All involved modules change |
| Interface simplicity | Simple — fewer exposed details | Complex — more details visible |
| Module independence | High — modules evolve separately | Low — modules are coupled |
| Detectability | Obvious when done well | Subtle — "back-door" leakage is pernicious |

Common causes of leakage:
- **[[temporal-decomposition]]** — splitting read from parse, write from format, when both phases share knowledge of the data structure
- **[[classitis]]** — too many small classes, each knowing a bit about the same thing
- **Exposed getters/setters** — private fields exposed through public accessors

The remedies when leakage is detected:
1. **Merge** the affected classes if they are small and closely tied to the leaked information
2. **Extract** the information into a new class with a simple interface that abstracts away the details

## When to Prioritize Hiding

- For any design decision likely to change (algorithms, data structures, external APIs)
- For details that callers don't need to know (disk block sizes, network protocols)
- For implementation choices that could have multiple valid approaches

## When Some Exposure Is Acceptable

- When callers genuinely need the information (performance tuning parameters)
- When hiding it would create a worse abstraction — a false [[abstractions|abstraction]] that pretends to hide what callers need to know
- When [[pull-complexity-downwards|pulling complexity down]] is not possible

The goal is to *minimize* information needed outside each module, not to hide everything. If information is needed, expose it explicitly rather than leaking it implicitly.

## Related
- [[information-hiding]] — full concept page
- [[information-leakage]] — full concept page
- [[deep-modules]] — what hiding produces
- [[shallow-modules]] — what leakage produces
- [[temporal-decomposition]] — a common cause of leakage
- [[a-philosophy-of-software-design-ch05]] — where both are analyzed
