---
title: "Chapter 12 - Why Write Comments? The Four Excuses"
tags: [chapter, software-design, documentation]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Chapter 12 - Why Write Comments? The Four Excuses

Part of [[a-philosophy-of-software-design]]

[[comments-and-documentation|Comments]] play a crucial role beyond helping developers understand code: they are essential for [[abstractions|abstraction]]. Without comments, you can't hide complexity — users must read implementation to use a module, and there is no abstraction. The informal aspects of an interface (behavior, constraints, rationale) can only be described in comments.

Four excuses for not writing comments:
1. **"Good code is self-documenting"** — Only the formal parts of an interface (signatures, types) can be expressed in code. Much design information (what a method does, why it was designed that way, when to call it) cannot be represented in code.
2. **"No time"** — Comments add ~10% to dev time and pay for themselves quickly. Interface comments are written during design and provide immediate value.
3. **"Comments get stale"** — Not a major problem in practice. Large doc changes only needed with large code changes. Code reviews catch stale comments.
4. **"Existing comments are worthless"** — This is a technique problem, not fundamental. Writing good comments is learnable.

Good documentation reduces [[cognitive-load]] (provides needed info without reading code) and [[unknown-unknowns]] (clarifies system structure). It clarifies dependencies and fills gaps to eliminate obscurity.

Ousterhout disagrees with Robert Martin's "comments are failures" view — they serve a fundamental role in defining abstractions and managing complexity. Code and comments each serve different purposes.

## Related
- [[comments-and-documentation]] — the comprehensive concept
- [[abstractions]] — what comments enable
- [[a-philosophy-of-software-design-ch13]] — how to write good comments
