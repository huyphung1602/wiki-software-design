---
title: Classitis
aliases: [class obsession, small class bias]
tags: [anti-pattern, modules, culture, design]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Classitis

Classitis is a cultural anti-pattern where developers believe "classes are good, so more classes are better." The result: systems decomposed into large numbers of small, [[shallow-modules]] that collectively generate more complexity than they hide.

The pattern is reinforced by conventional advice — "classes should be small," "any method longer than N lines should be split." This produces individually simple classes but increases overall system complexity. Each small class contributes little functionality, so there must be many of them, each with its own interface. These interfaces accumulate at the system level. Small classes also create verbose programming styles from the boilerplate required for each class.

The Java I/O library is Ousterhout's example: to read serialized objects from a file, developers must create three separate objects (`FileInputStream`, `BufferedInputStream`, `ObjectInputStream`). The first two are never used after opening. Buffering must be explicitly requested — if forgotten, I/O silently becomes slow. Contrast this with Unix I/O, where one `open` call handles everything and sequential access (the common case) is the default.

The lesson: providing choice is good, but interfaces should make the common case simple. Almost everyone wants buffered I/O, so it should be the default. The few who don't can use a mechanism to disable it, cleanly separated so most developers never need to know it exists.

Classitis is the cultural root cause behind many [[shallow-modules]]. The antidote is [[deep-modules]] — fewer interfaces that each hide more complexity. Classitis also leads to [[information-leakage]]: too many small classes means knowledge gets spread across them. The HTTP server example shows this — splitting request reading from parsing duplicated HTTP structure knowledge across two classes.

## Related
- [[shallow-modules]] — the result of classitis
- [[deep-modules]] — the antidote
- [[information-leakage]] — what classitis causes
- [[modular-design]] — the design practice classitis distorts
- [[a-philosophy-of-software-design-ch04]] — where classitis is named
- [[a-philosophy-of-software-design-ch05]] — where it's connected to information leakage
- [[a-philosophy-of-software-design-ch07]] — decorators as a classitis pattern
