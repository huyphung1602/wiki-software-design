---
title: Generality vs Specialization
aliases: [specialization vs generality, general-purpose vs special-purpose]
tags: [comparison, modules, design, interface, complexity]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Generality vs Specialization

One of the most consequential design decisions: should a module's interface be tailored to its current use, or general enough to support multiple purposes? This comparison explores why the answer is almost always "somewhat general-purpose."

## Generality: general-purpose interfaces

Build modules whose interfaces are broad enough to support multiple uses while remaining easy for today's needs. Fewer methods with broader capability. The sweet spot is "somewhat general-purpose" — the interface should be general, but don't go so far that it becomes hard to use. See [[generality]] for the full concept.

## Specialization: special-purpose interfaces

Tailor interfaces to specific use cases. Methods map directly to visible features (e.g., `backspace()`, `deleteSelection()`). Seems easier at first because each method does exactly one thing the caller needs. See [[specialization]] for the full concept.

## The Tension

The counterintuitive finding: **general-purpose code is simpler than special-purpose code**, even when only used in one specific way. The text editor example from Ousterhout's course proves this:

| Aspect | Specialized API | General-Purpose API |
|--------|----------------|-------------------|
| Methods for modifying text | `backspace()`, `delete()`, `deleteSelection()` | `insert(Position, String)`, `delete(Position, Position)` |
| Total methods | More (3+ for deletion alone) | Fewer (1 for all deletions) |
| Total code | More code overall | Less code overall |
| Information hiding | Poor — UI concepts leak into text class | Good — text class knows nothing about UI |
| Cognitive load | High — many shallow methods to learn | Low — few deep methods to learn |
| Reusability | Low — tied to one use case | High — works for editors, batch processing, search |

Three questions to guide the balance:
1. **What is the simplest interface covering all current needs?** Fewer methods with broader capability = more general.
2. **In how many situations will this method be used?** A method designed for one particular use is a [[red-flags|red flag]].
3. **Is this API easy to use for current needs?** If you need lots of extra code to use it, the interface may be too abstract.

## When to Favor Generality

- Almost always. The default should be "somewhat general-purpose."
- When designing lower-level modules that will be used by multiple higher-level modules.
- When the cost of generality is low (fewer methods, less code).

## When Specialization Is Acceptable

- At the top of the software stack (application-level features are necessarily specialized).
- When the special-purpose code is cleanly separated from general-purpose code — push it upward or downward.
- When a module truly has only one use case and the interface would become confusing if made more general.

The key insight: specialization is inevitable, but it must be **contained**. Push specialized code to the boundaries — up into top-level application classes or down into device-specific drivers — so it doesn't leak into the general-purpose core.

## Related
- [[generality]] — full concept page
- [[specialization]] — full concept page
- [[deep-modules]] — generality produces deeper modules
- [[shallow-modules]] — specialization produces shallower ones
- [[information-hiding]] — generality hides more
- [[information-leakage]] — specialization causes leakage
- [[classitis]] — cultural pressure toward over-specialization
- [[a-philosophy-of-software-design-ch06]] — where this tension is explored
