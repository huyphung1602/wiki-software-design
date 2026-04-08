---
title: Comments and Documentation
aliases: [code documentation, code comments]
tags: [core-concept, documentation, design, abstractions]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Comments and Documentation

Comments are essential for managing [[complexity]]. They serve three roles: helping developers understand the system, enabling [[abstractions|abstraction]] (without comments, you can't hide complexity), and improving system design (the act of writing comments reveals design problems).

Four excuses for not writing comments, all debunked:
- **"Good code is self-documenting"** — Code can only express the formal parts of an interface. The informal aspects (behavior, constraints, rationale) require comments. If users must read implementation to use a method, there is no abstraction.
- **"No time"** — Comments add ~10% to development time (upper bound) and pay for themselves quickly. The most important comments (interface docs) are written during design and pay off immediately.
- **"Comments get stale"** — Keeping docs updated is not hard if done alongside code changes. Code reviews catch stale comments.
- **"Existing comments are worthless"** — This reflects poor commenting technique, not a fundamental problem. Good comments are not hard to write.

The guiding principle: **describe things that aren't obvious from the code.** Comments should operate at a different level of detail than the code:

**Lower-level comments add precision:** units, boundary conditions (inclusive/exclusive), null meaning, resource ownership, invariants. Variable comments should describe *what* the variable represents (nouns), not how it's manipulated (verbs).

**Higher-level comments enhance intuition:** overall intent, why code exists, conceptual framework. Instead of narrating each line, express the one simple idea that explains the whole block.

**Interface comments define abstractions.** They must be separate from implementation comments. If interface comments must describe implementation details, the class is shallow — a design clue. Method interface comments should cover: overall behavior, arguments and return values (precisely), side effects, exceptions, and preconditions.

**Implementation comments** should explain what and why, not how. For longer methods, comment each major block at a higher level.

**Cross-module decisions** are the hardest to document. Use a central `designNotes` file with clearly labeled sections, referenced from code.

Ousterhout explicitly disagrees with Robert Martin's view that "comments are failures." Comments and code serve different purposes — code is precise but low-level, comments are less precise but provide intuitive understanding and capture design rationale.

## Related
- [[abstractions]] — comments are what make abstractions possible
- [[deep-modules]] — good comments define the interface that creates depth
- [[complexity]] — what documentation helps manage
- [[red-flags]] — comment repeats code, implementation docs contaminate interface
- [[a-philosophy-of-software-design-ch12]] — why comments matter
- [[a-philosophy-of-software-design-ch13]] — how to write good comments
- [[a-philosophy-of-software-design-ch16]] — maintaining comments when modifying existing code
- [[obvious-code]] — comments compensate for unavoidable nonobviousness
