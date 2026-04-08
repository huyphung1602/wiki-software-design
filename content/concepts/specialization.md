---
title: Specialization
aliases: [special-purpose design, specific design]
tags: [anti-pattern, modules, design, interface]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Specialization

Specialization in software design means tailoring modules, methods, or code to specific use cases rather than making them general-purpose. Ousterhout identifies over-specialization as "perhaps the single greatest cause of [[complexity]] in software." Specialized code tends to have more methods, shallower interfaces, and worse [[information-hiding]].

The problems with specialization:

1. **More methods, less capability** — A specialized text class has `backspace()`, `delete()`, `deleteSelection()` — three methods for variations of the same operation. A [[generality|general-purpose]] version has a single `delete(Position, Position)` that handles all three cases.
2. **False abstractions** — Specialized methods like `backspace()` purport to hide which characters are deleted, but UI developers actually need to know this. They'll read the implementation anyway. The abstraction adds obscurity rather than reducing it.
3. **Information leakage** — Specialization causes UI concepts (backspace key, selection) to leak into lower-level modules like the text class, creating coupling between modules that should be independent.
4. **More code overall** — Counterintuitively, specialized approaches produce more total code than [[generality|general-purpose]] ones, because each special case requires its own method.

Specialization can't be eliminated entirely, but it should be **separated** from general-purpose code. Push it upward (top-level classes are specialized, don't leak into lower layers) or downward (device drivers implement a general interface using specialized commands). The History class example shows this: a general-purpose `History` class manages action lists, while special-purpose undo actions live in their respective modules.

Beyond class design, **eliminate special cases in code**. An empty selection isn't a special state — it's a selection with the same start and end position. Design the normal case to handle edge conditions automatically.

See [[generality-vs-specialization]] for the full comparison.

## Related
- [[generality]] — the preferred approach
- [[generality-vs-specialization]] — comparison of both approaches
- [[shallow-modules]] — specialization produces shallow modules
- [[information-leakage]] — specialization causes leakage
- [[classitis]] — cultural pressure toward over-specialization
- [[complexity]] — what over-specialization causes
- [[together-or-apart]] — whether to combine or separate functionality
- [[a-philosophy-of-software-design-ch06]] — where specialization's problems are analyzed
