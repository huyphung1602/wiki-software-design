---
title: Shallow Modules
aliases: [thin abstraction, shallow abstraction]
tags: [anti-pattern, modules, design]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Shallow Modules

A shallow module has an interface that is relatively complex compared to the functionality it provides. It is the opposite of [[deep-modules]] — the interface exposes nearly as much complexity as the implementation hides. Shallow modules fail at the core purpose of [[modular-design]]: they add interface complexity to the system without a compensating reduction in implementation complexity.

Linked lists are a typical example — inserting or deleting takes a few lines of code, so the linked list abstraction hides almost nothing. The interface complexity nearly equals the implementation complexity. Such modules can be useful and sometimes unavoidable, but they provide little leverage against [[complexity]].

The extreme case is a trivial wrapper method like `addNullValueForAttribute` that just calls `data.put(attribute, null)`. Ousterhout argues this makes things worse, not better: it offers no abstraction (all functionality is visible through the interface), adds a new interface for developers to learn, and takes more keystrokes to invoke than direct access would. The method adds complexity with no compensating benefit.

**Red Flag: Shallow Module** — if a module's interface is complicated relative to its functionality, it's not paying its way. Small modules tend to be shallow.

The systemic version of this problem is [[classitis]] — a cultural bias toward many small classes that collectively generate enormous interface complexity.

[[information-leakage|Leaked information]] also produces shallow modules: when a design decision is reflected in multiple modules, each module has a wider interface relative to its own functionality. [[temporal-decomposition]] is a common cause — splitting reading from parsing duplicates knowledge across classes.

## Related
- [[deep-modules]] — the ideal, what shallow modules fail to be
- [[classitis]] — the cultural pattern that produces many shallow modules
- [[complexity]] — what shallow modules fail to manage
- [[information-leakage]] — a cause of shallowness
- [[temporal-decomposition]] — a pattern that produces shallow modules
- [[red-flags]] — shallow module is a recognized red flag
- [[a-philosophy-of-software-design-ch04]] — where this anti-pattern is defined
- [[a-philosophy-of-software-design-ch05]] — where leakage as a cause is analyzed
- [[a-philosophy-of-software-design-ch19]] — getters and setters as a shallow pattern
- [[decide-what-matters]] — treating too many things as important creates shallow modules
- [[deep-modules-vs-shallow-modules]] — comparison with the ideal
