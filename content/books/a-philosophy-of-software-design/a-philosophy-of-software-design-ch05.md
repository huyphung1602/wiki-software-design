---
title: "Chapter 5 - Information Hiding (and Leakage)"
tags: [chapter, software-design, modules]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Chapter 5 - Information Hiding (and Leakage)

Part of [[a-philosophy-of-software-design]]

This chapter presents the primary technique for creating [[deep-modules]]: [[information-hiding|information hiding]]. Each module should encapsulate design decisions as knowledge in its implementation, keeping them out of its interface. Hidden knowledge includes data structures, algorithms, and assumptions. Information hiding reduces [[complexity]] by simplifying interfaces and making the system easier to evolve.

Private declarations are not the same as [[information-hiding|information hiding]] — getters and setters can expose information just as much as public fields. The best hiding makes information totally invisible and irrelevant. Partial hiding (features needed by few users, accessed through separate methods) also has value.

The opposite is [[information-leakage]]: a design decision reflected in multiple modules. This creates a dependency across all involved modules. Leakage can happen through interfaces (obvious) or "back-door" (two classes sharing knowledge of a file format — more pernicious because invisible). Three [[red-flags]] from this chapter: information leakage, [[temporal-decomposition]] (structure follows execution order), and overexposure (common features force learning about rare ones).

The HTTP server examples are instructive. Splitting request reading from parsing duplicated knowledge — temporal decomposition. Returning `getParams()` as a `Map` exposed internal representation; `getParameter(name)` hides it. Auto-providing HTTP version and Date headers (defaults) follows the principle: "do the right thing without being asked."

[[information-hiding|Information hiding]] can be applied within a class too — private methods should encapsulate knowledge, and instance variable usage should be minimized. But don't hide information needed outside the module. The goal is to minimize what's needed externally, not to hide everything.

## Related
- [[information-hiding]] — the core technique
- [[information-leakage]] — the anti-pattern
- [[temporal-decomposition]] — a common cause of leakage
- [[deep-modules]] — what information hiding produces
- [[red-flags]] — three new flags from this chapter
