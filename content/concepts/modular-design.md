---
title: Modular Design
aliases: [modularity, module design]
tags: [core-concept, design, modules, encapsulation]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Modular Design

Modular design is one of the two fundamental approaches to managing [[complexity]] (the other being simplification). The idea: divide a software system into modules (classes, subsystems, services) that are relatively independent, so a developer can work in one module without understanding the details of others.

Each module has an **interface** (what others must know to use it) and an **implementation** (the code that carries out the interface's promises). Interfaces contain formal elements (signatures, types) and informal elements (behavior, constraints). The informal aspects are usually larger and more complex — they require comments, not just code.

The goal is to minimize dependencies between modules. Developers should understand the interface and implementation of the module they're working on, plus only the interfaces of modules they invoke — never the implementations of other modules.

The key metric is **depth**: [[deep-modules]] (simple interface, complex implementation) maximize the complexity hidden per unit of interface exposed. [[Shallow-modules]] do the opposite. The cultural bias toward many small classes — [[classitis]] — produces shallow modules whose interfaces accumulate into system-level complexity.

Good [[abstractions]] are the result: simplified views that omit unimportant details while preserving everything that matters. Information should be hidden within modules, not leaked across them. Modules should be general-purpose, not narrowly tailored to current needs.

## Related
- [[complexity]] — what modular design encapsulates
- [[deep-modules]] — the ideal form of a module
- [[shallow-modules]] — the anti-pattern
- [[abstractions]] — the conceptual foundation
- [[problem-decomposition]] — the skill that produces good module boundaries
- [[a-philosophy-of-software-design-ch01]] — where modular design is introduced
- [[a-philosophy-of-software-design-ch04]] — where depth, interfaces, and abstractions are developed
