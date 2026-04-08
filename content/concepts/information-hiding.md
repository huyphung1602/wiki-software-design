---
title: Information Hiding
aliases: [encapsulation, data hiding, information encapsulation]
tags: [core-concept, modules, design, encapsulation]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Information Hiding

Information hiding is the primary technique for achieving [[deep-modules]]. First described by David Parnas (1972), the idea is that each module should encapsulate a few pieces of knowledge — design decisions — in its implementation, keeping them out of its interface and invisible to other modules.

Hidden knowledge typically includes data structures, algorithms, lower-level details (page sizes), and higher-level assumptions ("most files are small"). Information hiding reduces [[complexity]] in two ways:

1. **Simpler interfaces** — The interface reflects a simpler, more abstract view, reducing [[cognitive-load]] on developers using the module. A developer using a B-tree class need not worry about fanout or rebalancing.
2. **Easier evolution** — If information is hidden, there are no dependencies on it outside the module. Changes affect only one module. If TCP changes its congestion control, higher-level code using TCP should not need modification.

**Private ≠ hidden.** Declaring fields private is not the same as information hiding. If public getters and setters expose the nature and usage of a variable, the information is just as exposed as if the variable were public. The best form of hiding is when information is totally invisible and irrelevant to module users.

**Partial information hiding** also has value. If a feature is only needed by a few of a class's users and accessed through separate methods (so it isn't visible in the most common use cases), that information is mostly hidden and creates fewer dependencies.

Information hiding can be applied at multiple levels — not just between classes, but within a class. Private methods should each encapsulate some information, and the number of places where each instance variable is used should be minimized.

The technique has limits: don't hide information that is needed outside the module. If performance tuning requires configuration, expose it. The goal is to *minimize* information needed outside, not to hide everything.

[[generality|General-purpose interfaces]] improve information hiding. A special-purpose interface tied to current use cases leaks details about those uses into the module (e.g., a `backspace()` method in a text class leaks UI knowledge). A general-purpose interface (`delete(Position, Position)`) keeps the module unaware of higher-level concerns, enabling better separation and more hidden information.

## Related
- [[deep-modules]] — what information hiding produces
- [[information-leakage]] — the anti-pattern, the opposite
- [[modular-design]] — the framework
- [[complexity]] — what information hiding reduces
- [[a-philosophy-of-software-design-ch05]] — where this technique is developed
- [[a-philosophy-of-software-design-ch19]] — OOP mechanisms support information hiding when used correctly
- [[decide-what-matters]] — hiding what does not matter to module users
- [[obvious-code]] — obvious code reduces information readers need
- [[information-hiding-vs-information-leakage]] — comparison with the anti-pattern
