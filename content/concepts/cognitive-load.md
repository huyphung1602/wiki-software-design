---
title: Cognitive Load
aliases: [mental load, developer cognitive load]
tags: [symptom, complexity, developer-experience]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Cognitive Load

Cognitive load is the second symptom of [[complexity]]: how much a developer needs to know in order to complete a task. Higher cognitive load means more time learning required information and greater risk of bugs from missing something important.

Ousterhout's example: a C function that allocates memory and assumes the caller will free it. This adds cognitive load — if the caller forgets, there's a memory leak. Restructuring so the same module allocates and frees reduces cognitive load.

**Lines of code is a misleading measure.** Ousterhout has seen frameworks where applications could be written in a few lines, but figuring out *what* those lines should be was extremely difficult. Sometimes an approach requiring more lines of code is actually simpler because it reduces cognitive load.

Cognitive load arises from: APIs with many methods, global variables, inconsistencies, and dependencies between modules. A high cognitive load increases the cost of a change, but if it's clear which information to read, the change is still likely to be correct. This makes it less dangerous than [[unknown-unknowns]].

## Related
- [[complexity]] — the problem this symptom signals
- [[change-amplification]] — the first symptom
- [[unknown-unknowns]] — the worst symptom
- [[a-philosophy-of-software-design-ch02]] — where this is defined
