---
title: "Ch 6: General-Purpose Modules are Deeper"
tags: [chapter, software-design, modules]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Ch 6: General-Purpose Modules are Deeper

Part of [[a-philosophy-of-software-design]]

Ousterhout identifies over-specialization as perhaps the single greatest cause of [[complexity]]. General-purpose code is simpler, cleaner, and easier to understand. The principle applies at every level: class design, method APIs, and code within method bodies.

The sweet spot is **"somewhat general-purpose"**: functionality reflects current needs, but the interface should not be tied to them. Surprisingly, even when used in a special-purpose way, a general-purpose class is less work to build. The text editor example: `backspace()`, `delete()`, `deleteSelection()` (three shallow methods leaking UI into text class) vs. `insert(Position, String)` + `delete(Position, Position)` (two general methods, less code overall, better [[information-hiding]]).

[[generality|Generality]] leads to better [[deep-modules|depth]] and information hiding. The special-purpose `backspace()` method was a false [[abstractions|abstraction]] — it hid behavior the UI developers needed to know, forcing them to read the implementation anyway. When details matter, make them explicit and obvious rather than hiding them behind a misleading interface.

Specialization is inevitable but should be separated from general-purpose code. Push it upward (top-level classes are specialized, don't leak down) or downward (device drivers implement general interfaces with specialized commands). The editor undo example: a general-purpose `History` class manages action lists while special-purpose undo actions (`UndoableInsert`, `UndoableSelection`) live in their respective modules — clean separation of mechanism, specifics, and policy.

Beyond class design: **eliminate special cases in code**. Empty selection = selection with same start/end position. Design the normal case to handle edge conditions automatically. Three design questions: simplest interface covering all needs? How many situations will this method serve? Is this API easy for current needs?

## Related
- [[generality]] — the core principle
- [[specialization]] — separating specialized from general-purpose code
- [[generality-vs-specialization]] — comparison of the trade-off
- [[deep-modules]] — generality produces depth
- [[information-hiding]] — general interfaces hide more
- [[abstractions]] — specialization creates false abstractions
- [[a-philosophy-of-software-design-ch05]] — information hiding, the foundation
