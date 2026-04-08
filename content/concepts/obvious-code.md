---
title: Obvious Code
aliases: [readable code, self-documenting code]
tags: [core-concept, readability, code-quality]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Obvious Code

Code is obvious when a reader can understand it quickly, without much thought, and their first guess about its behavior will be correct. Obviousness is the antidote to obscurity, which is one of the two root causes of [[complexity]] (the other being dependencies). When code is not obvious, readers must expend significant time and energy to understand it, reducing efficiency and increasing the likelihood of misunderstanding and bugs.

## The Reader's Perspective

"Obvious" is defined by the reader, not the writer. It is easier to see that someone else's code is nonobvious than to recognize problems in your own. This makes code reviews the best tool for detecting nonobviousness: if a reviewer says code is not obvious, it is not obvious, regardless of how clear it seems to the author. By understanding what made the code confusing, you learn to write better code.

## Techniques for Obviousness

Three strategies make code more obvious. The best is to reduce the information readers need, using [[abstractions|abstraction]] and eliminating special cases. The second is to leverage information readers already have through [[consistency|conventions]] and conformance to expectations. The third is to present essential information directly through [[choosing-names|good names]], whitespace, and strategic [[comments-and-documentation|comments]].

## Common Sources of Nonobviousness

Several patterns make code harder to understand: event-driven programming obscures control flow because handlers are invoked indirectly through function pointers or interfaces; generic containers (like `Pair`) hide meaning behind generic accessor names; mismatched declaration and allocation types mislead readers about how a variable behaves; and code that violates expectations (such as a constructor that creates background threads) must be explicitly documented. The general rule: design for ease of reading, not ease of writing.

## Related
- [[consistency]] -- a primary technique for achieving obviousness
- [[choosing-names]] -- precise names make behavior clear without reading code
- [[comments-and-documentation]] -- compensating for unavoidable nonobviousness
- [[complexity]] -- obscurity as a root cause
- [[red-flags]] -- nonobvious code is itself a red flag
- [[a-philosophy-of-software-design-ch18]] -- the source chapter
