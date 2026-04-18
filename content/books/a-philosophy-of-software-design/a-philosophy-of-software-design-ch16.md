---
title: "Chapter 16 - Modifying Existing Code"
tags: [software-design, refactoring, documentation]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Chapter 16 - Modifying Existing Code

Part of [[a-philosophy-of-software-design]]

Software systems evolve through many small changes, and the design of a mature system is shaped more by how those changes are made than by any initial plan. This chapter argues that the same [[strategic-programming|strategic mindset]] needed for initial design must be applied every time existing code is modified.

## Stay Strategic

The typical developer approach to modifying existing code is tactical: "what is the smallest change I can make?" This minimizes risk in the short term but accumulates [[complexity]] through special cases and dependencies. The strategic alternative is to refactor so the system ends up with the structure it would have had if designed correctly from the start. This is the [[continuous-design|investment mindset]] in action -- each change should leave the design at least a little better. If you are not improving the design, you are probably making it worse.

## Maintaining Comments

Code changes invalidate existing comments. Several techniques keep documentation alive: place comments as close as possible to the code they describe; put interface comments in code files, not separate header files; spread implementation comments to the narrowest scope; and avoid duplicating documentation -- document each design decision in exactly one obvious place. Comments should go in the code, not in commit logs, because developers rarely scan repository history. Higher-level, more abstract comments are easier to maintain because minor code changes do not affect them.

## Checking Diffs

Before committing changes, scan all modifications to ensure documentation stays consistent. This pre-commit review also catches debugging leftovers and unresolved TODO items.

## Related
- [[strategic-programming]] -- the mindset required for every code change
- [[continuous-design]] -- design improves incrementally with each modification
- [[comments-and-documentation]] -- maintaining comments during code evolution
- [[complexity]] -- accumulates when changes are tactical
- [[design-investment]] -- investing extra time in refactoring pays off
