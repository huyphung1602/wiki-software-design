---
title: Comments-First Approach
aliases: [comments first, document first]
tags: [core-concept, documentation, design-process]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Comments-First Approach

Write [[comments-and-documentation|comments]] at the beginning of the development process, not the end. The workflow: class interface comment → method interface comments and signatures (empty bodies) → iterate on structure → instance variable comments → fill in method bodies with implementation comments. When code is done, comments are done.

Delayed comments are bad comments. Written at the end, they repeat the code (because you look at code to write them), miss design rationale (because you've forgotten it), and often never get written (because the backlog becomes daunting).

The approach produces better comments (design is fresh, you focus on [[abstractions|abstraction]] not implementation), better design (comments are a canary for complexity — if a method needs a long interface comment, the design needs work), and makes documentation more enjoyable (designing abstractions is the fun part, and comments are how you evaluate designs).

Comments as a design tool: if you can't describe a method simply and completely, the [[red-flags|design has problems]]. The simpler the comments, the better the design. Writing comments first lets you evaluate and fix design decisions before investing in implementation code.

## Related
- [[comments-and-documentation]] — the role comments serve
- [[continuous-design]] — comments-first as a continuous design practice
- [[strategic-programming]] — the investment mindset that enables this approach
- [[a-philosophy-of-software-design-ch15]] — where this approach is introduced
