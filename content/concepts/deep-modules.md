---
title: Deep Modules
aliases: [deep abstraction, thick interface]
tags: [core-concept, modules, design, encapsulation]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Deep Modules

A deep module provides powerful functionality through a simple interface. It is the ideal form of [[modular-design]] — maximum benefit (functionality) at minimum cost (interface complexity). The "depth" metaphor comes from imagining modules as rectangles: the top edge is the interface, the area is the functionality. Deep modules have a narrow top edge sitting on a large rectangle.

The canonical example is Unix file I/O: five system calls (`open`, `read`, `write`, `lseek`, `close`) with simple signatures, backed by hundreds of thousands of lines of implementation handling disk layout, permissions, caching, concurrent access, and device abstraction. The interface has barely changed in decades while implementations have evolved radically. An even deeper module is a garbage collector — it has no interface at all, yet hides enormous complexity.

Depth is a cost-benefit calculation. The benefit of a module is its functionality. The cost (in system complexity) is its interface — what other developers must learn and depend on. Deep modules maximize this ratio. They are good [[abstractions]] because only a small fraction of internal complexity is visible to users.

Key properties:
- Simple interfaces for common cases, with advanced features available but not prominent
- Effective interface complexity equals the complexity of commonly used features
- Many internal aspects can change without affecting other modules

Deep modules are the primary mechanism for managing [[complexity]]. They reduce [[cognitive-load]] (developers see only the interface), minimize [[change-amplification]] (internal changes don't propagate), and eliminate [[unknown-unknowns]] (the interface specifies exactly what users need to know).

The primary technique for achieving depth is [[information-hiding]]: encapsulate design decisions as knowledge within the module, keeping them out of the interface. The more information hidden, the deeper the module. Conversely, [[information-leakage]] prevents depth — if knowledge is reflected in multiple modules, each has a wider interface relative to its functionality.

[[generality|General-purpose interfaces]] are another path to depth. A somewhat general-purpose interface — one that covers current needs without being tied to them — results in fewer methods, each more broadly useful, with less code overall. The text editor example: three special-purpose methods (`backspace`, `delete`, `deleteSelection`) replaced by two general ones (`insert`, `delete`) that handle more cases with less code.

## Related
- [[modular-design]] — the broader framework depth belongs to
- [[shallow-modules]] — the anti-pattern, the opposite of depth
- [[abstractions]] — deep modules are good abstractions
- [[classitis]] — the cultural bias that produces shallow modules
- [[information-hiding]] — the primary technique for achieving depth
- [[a-philosophy-of-software-design-ch04]] — where depth is defined
- [[a-philosophy-of-software-design-ch05]] — where the technique for creating deep modules is developed
- [[a-philosophy-of-software-design-ch08]] — pulling complexity down as another path to depth
- [[deep-modules-vs-shallow-modules]] — comparison with the anti-pattern
- [[designing-for-performance]] — deep modules are naturally more efficient than shallow ones
