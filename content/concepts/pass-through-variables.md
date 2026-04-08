---
title: Pass-Through Variables
aliases: [threaded variables, context variables]
tags: [anti-pattern, design, variables]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Pass-Through Variables

A pass-through variable is passed down through a long chain of methods but only needed at the bottom. Every intermediate method must include it in its signature and be aware of its existence, adding complexity without contributing to those methods' functionality.

Adding a new pass-through variable requires modifying a large number of interfaces and methods. This is a form of [[change-amplification]] and a symptom that the layer structure doesn't properly encapsulate the information.

Solutions, from worst to best:
1. **Shared object** — If topmost and bottommost methods already share an object, store the variable there. But the shared object may itself be a pass-through variable.
2. **Global variable** — Avoids passing, but creates problems: can't have multiple instances in one process (breaks testing), non-obvious dependencies.
3. **Context object** — The best available solution. A single object stores all application global state (configuration, shared subsystems, performance counters). One context per system instance, allowing coexistence in a single process. Adding new variables only requires modifying the context's constructor.

Context objects are far from ideal — they have most disadvantages of global variables (unclear why a variable exists, where it's used, potential for becoming a grab-bag, thread-safety issues). Making context variables immutable helps. But no better solution has been found.

The context reference can be stored in major objects as an instance variable, passed only in constructors, so it doesn't appear as an explicit argument in most methods.

## Related
- [[pass-through-methods]] — the method analogue
- [[change-amplification]] — what pass-through variables cause
- [[complexity]] — the underlying problem
- [[a-philosophy-of-software-design-ch07]] — where this is analyzed
