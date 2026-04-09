---
title: "Ch 4: Modules Should Be Deep"
tags: [chapter, software-design, modules]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Ch 4: Modules Should Be Deep

Part of [[a-philosophy-of-software-design]]

This chapter introduces the foundational technique for managing [[complexity]]: [[modular-design]], where each module has an interface (what others must know) and an implementation (how it works). The goal is to minimize dependencies between modules so developers need understand only the module they're working on plus the interfaces of modules they use.

Interfaces contain both formal elements (signatures, types — enforced by the language) and informal elements (behavior, constraints — described in comments). The informal aspects are usually larger and more complex. Well-specified interfaces help eliminate [[unknown-unknowns]] by indicating exactly what developers need to know.

The chapter's central concept is module depth. [[Deep-modules]] provide powerful functionality through simple interfaces — Unix I/O is the example, with five system calls backed by hundreds of thousands of lines. [[Shallow-modules]] are the anti-pattern: complex interfaces relative to the functionality they provide, adding system complexity without compensating benefit. A trivial wrapper method that just delegates to a data structure is worse than useless — it adds an interface to learn while hiding nothing.

[[Abstractions]] can fail two ways: including unimportant details (bloats cognitive load) or omitting important ones (false abstraction, creates obscurity). The key design skill is understanding what matters and minimizing that set.

The chapter names [[classitis|classitis]] as the cultural disease producing shallow modules: the belief that "classes are good, so more classes are better." Java I/O (three objects to open a buffered file) vs. Unix I/O (one call) illustrates the contrast. The principle: make the common case simple, keep advanced features available but out of the way.

## Related
- [[modular-design]] — the framework this chapter builds on
- [[deep-modules]] — the chapter's signature concept
- [[shallow-modules]] — the anti-pattern
- [[classitis]] — the cultural source of shallow modules
- [[abstractions]] — the conceptual foundation
- [[complexity]] — what deep modules reduce
