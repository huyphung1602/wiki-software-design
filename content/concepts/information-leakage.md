---
title: Information Leakage
aliases: [knowledge leakage, implementation leakage]
tags: [anti-pattern, modules, design, red-flag]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Information Leakage

Information leakage is the opposite of [[information-hiding]]: a design decision is reflected in multiple modules. This creates a dependency — any change to that design decision requires changes to all involved modules.

If information appears in a module's interface, it has leaked by definition (simpler interfaces correlate with better hiding). But information can leak even without appearing in interfaces — "back-door" leakage. If two classes both understand a file format (one reads, one writes), they both depend on it even if neither exposes the format in its interface. Back-door leakage is more pernicious because it isn't obvious.

Information leakage is one of the most important [[red-flags]]. Developing sensitivity to it is one of the best skills a software designer can learn. When you encounter leakage, ask: "How can I reorganize so this knowledge affects only a single class?" Two remedies:
- **Merge** the affected classes if they are small and closely tied to the leaked information
- **Extract** the information into a new class — but only if you can find a simple interface that abstracts away the details. Otherwise you've just replaced back-door leakage with interface leakage.

A common cause is [[temporal-decomposition]], where structure follows execution order rather than knowledge boundaries. [[classitis|Too many small classes]] also leads to leakage, as the HTTP server example shows: splitting request reading from parsing duplicated knowledge of HTTP request structure across two classes.

The `getParams()` example illustrates leakage through interface: returning the internal `Map<String,String>` exposes the representation. Any change to how parameters are stored breaks the interface. `getParameter(name)` hides the representation.

## Related
- [[information-hiding]] — the practice leakage violates
- [[temporal-decomposition]] — a common cause of leakage
- [[deep-modules]] — what leakage prevents
- [[red-flags]] — leakage as a recognized red flag
- [[a-philosophy-of-software-design-ch05]] — where leakage is analyzed
- [[information-hiding-vs-information-leakage]] — comparison with the practice it violates
