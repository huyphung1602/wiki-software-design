---
title: Generality
aliases: [general-purpose design, generic design]
tags: [core-concept, modules, design, interface]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Generality

Generality in software design means building modules whose interfaces are general enough to support multiple uses while remaining easy for today's needs. Ousterhout argues that general-purpose code is simpler, cleaner, and easier to understand than [[specialization|special-purpose code]] — even when the class is only used in one specific way.

The sweet spot is **"somewhat general-purpose"**: module functionality should reflect current needs, but its interface should not be tied to them. The word "somewhat" matters — don't go so far that the class becomes difficult to use for current needs.

A surprising finding: even when a class is used in a special-purpose way, it is less work to build it in a general-purpose way. The text editor example demonstrates this. A special-purpose text class had `backspace()`, `delete()`, and `deleteSelection()` — three shallow methods tying UI concepts to text internals. The general-purpose version had `insert(Position, String)` and `delete(Position, Position)` — two methods that handle everything with less code overall and better [[information-hiding]].

Generality produces [[deep-modules]] because general-purpose interfaces hide more implementation detail. The [[abstractions]] are genuine — they omit truly unimportant details. Specialized interfaces, by contrast, create false abstractions that hide information the caller actually needs.

See [[generality-vs-specialization]] for the full comparison.

## Related
- [[specialization]] — the opposite tendency
- [[generality-vs-specialization]] — comparison of both approaches
- [[deep-modules]] — generality produces deeper modules
- [[information-hiding]] — general-purpose interfaces hide more
- [[abstractions]] — generality creates genuine abstractions
- [[together-or-apart]] — whether to combine or separate functionality
- [[red-flags]] — one-use methods and hard-to-use APIs are red flags
- [[a-philosophy-of-software-design-ch06]] — where generality is developed
