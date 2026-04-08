---
title: Abstractions
aliases: [abstraction, abstract interfaces]
tags: [core-concept, design, interface]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Abstractions

An abstraction is a simplified view of an entity that omits unimportant details. In [[modular-design]], each module provides an abstraction through its interface — a simplified view of the module's functionality where implementation details are hidden.

The word "unimportant" is crucial. The more unimportant details omitted from an abstraction, the better. But a detail can only be omitted if it truly is unimportant. Abstractions can go wrong in two ways:

1. **Including unimportant details** — makes the abstraction more complicated than necessary, increasing [[cognitive-load]] on developers using it
2. **Omitting important details** — creates a false abstraction that appears simple but isn't. Developers looking only at the abstraction won't have all the information they need. This is a form of obscurity and a source of [[unknown-unknowns]]

The file system illustrates both. Its abstraction correctly omits block allocation (unimportant to users), but caching behavior must be visible — databases need to know when data is actually written to storage. Flushing rules cannot be hidden because they are important to some users.

Module interfaces contain both **formal** elements (signatures, types — specified in code, checked by the language) and **informal** elements (behavior, constraints, usage requirements — described in comments, not machine-checkable). For most interfaces, the informal aspects are larger and more complex than the formal aspects. This is why comments and documentation are essential to good abstractions.

The key design skill: understanding what is important and finding designs that minimize the amount of information that is important. [[Deep-modules]] are good abstractions — they omit the maximum amount of unimportant detail while preserving everything that matters.

Specialization creates false abstractions. A text class with a `backspace()` method purports to hide which characters are deleted, but UI developers need to know this — they'll read the implementation anyway. The abstraction adds obscurity rather than reducing it. A general-purpose `delete(start, end)` is a better abstraction: it doesn't pretend to hide what the caller needs to know. When details are important, make them explicit and obvious rather than hiding them behind a misleading interface.

## Related
- [[modular-design]] — the framework where abstractions operate
- [[deep-modules]] — the ideal abstraction
- [[unknown-unknowns]] — what false abstractions create
- [[cognitive-load]] — what good abstractions reduce
- [[a-philosophy-of-software-design-ch04]] — where abstractions are analyzed
- [[decide-what-matters]] — interfaces reflect what matters, implementations hide the rest
- [[designing-for-performance]] — performance optimization must preserve clean abstractions
- [[obvious-code]] — good abstractions reduce information readers need
