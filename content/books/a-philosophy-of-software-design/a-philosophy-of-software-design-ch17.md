---
title: "Chapter 17 - Consistency"
tags: [software-design, consistency, coding-style]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Chapter 17 - Consistency

Part of [[a-philosophy-of-software-design]]

[[consistency|Consistency]] is a powerful tool for reducing [[complexity]] and making system behavior more obvious. When similar things are done in similar ways, developers gain cognitive leverage: knowledge from one area transfers immediately to others. Consistency also reduces mistakes, because assumptions based on familiar-looking code patterns are safe.

## Where Consistency Applies

Consistency operates at many levels: naming conventions, coding style, interface design, use of [[abstractions|design patterns]], and invariants. [[choosing-names|Consistent names]] let readers recognize patterns without analyzing code. Consistent interfaces mean that learning one implementation teaches you about all others. Invariants -- properties that are always true -- reduce special cases and make reasoning easier.

## Ensuring Consistency

Maintaining consistency across a large team is hard. Three techniques help: document conventions where developers will see them; enforce conventions with automated tools (linters, pre-commit hooks) so violations cannot enter the codebase; and follow the "when in Rome" rule -- look at existing code in each file and match its patterns. Resist changing existing conventions unless you have significant new information and are willing to update all existing uses.

## Going Too Far

Consistency requires that dissimilar things be done in different ways. Forcing different problems into the same pattern creates confusion. Benefits only accrue when developers can trust that "if it looks like an X, it really is an X."

## Related
- [[consistency]] -- the concept page for this chapter's core idea
- [[choosing-names]] -- consistent naming as a design principle
- [[abstractions]] -- consistent interfaces multiply understanding
- [[continuous-design]] -- consistency as an ongoing investment
- [[complexity]] -- what consistency reduces
