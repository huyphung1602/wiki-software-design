---
title: Comments and Documentation
aliases: [code documentation, code comments]
tags: [core-concept, documentation, design, abstractions]
sources: [a-philosophy-of-software-design, naur]
created: 2026-04-08
updated: 2026-04-15
---

# Comments and Documentation

## In A Philosophy of Software Design

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

## In Programming as Theory Building

Naur's position is more radical: documentation is not just imperfect — it is fundamentally insufficient. The theory that programmers hold cannot be expressed in documentation at all. Documentation can jog memories and set up pathways of thought, but the theory itself is tacit: it exists only in the minds of programmers who have worked closely with the system.

The practical implication: even the most complete documentation — program text, annotated code, design discussions — cannot convey the deepest design ideas. This is why Naur's compiler case showed a team with full documentation still produced modifications that destroyed the original structure, while a team with personal guidance did not. Documentation's purpose, on Naur's view, is to help the next programmer build an adequate theory, not to carry the theory itself. The editor's commentary adds: documentation is always behind the current state of the program. Three minimal items help most: the metaphors, the purpose of each major component, and drawings of major interactions.

## Synthesis

Ousterhout and Naur agree that documentation matters but define its role differently. For Ousterhout, comments are essential interface-level artifacts that enable [[abstractions]] and reduce [[cognitive-load]]; good interface documentation separates the what from the how. For Naur, documentation is always auxiliary — it can support theory building but cannot substitute for the direct knowledge that theory requires. Both agree that the purpose of documentation is to help readers understand the system, not to describe the code: Ousterhout through precise interface contracts, Naur through jogging memories and setting up pathways. The tension resolves in practice: both are needed, but at different levels — Ousterhout's comments serve daily development, Naur's documentation serves theory transfer across team generations.

## Cases
- [[compiler-team-theory]] — group B had full annotated program texts, design discussions, and personal advice; still could not independently generate design judgments; demonstrates that no amount of documentation can substitute for personal contact with the theory holders (from Programming as Theory Building)
- [[industrial-monitoring-system]] — installation programmers could not name useful additional documentation; their knowledge came from continuous engagement, not documents; demonstrates that documentation is always behind the current state and cannot carry what continuous involvement builds (from Programming as Theory Building)

## Related
- [[abstractions]] — comments are what make abstractions possible
- [[deep-modules]] — good comments define the interface that creates depth
- [[complexity]] — what documentation helps manage
- [[red-flags]] — comment repeats code, implementation docs contaminate interface
- [[tacit-knowledge]] — why documentation cannot carry everything that matters
- [[naur-ch01]] — Naur's radical view of documentation's limitations
- [[naur-ch02]] — editor's advice on minimal documentation for theory building
- [[a-philosophy-of-software-design-ch12]] — why comments matter
- [[a-philosophy-of-software-design-ch13]] — how to write good comments
- [[a-philosophy-of-software-design-ch16]] — maintaining comments when modifying existing code
- [[obvious-code]] — comments compensate for unavoidable nonobviousness