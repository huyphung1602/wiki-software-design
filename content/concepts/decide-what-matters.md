---
title: Decide What Matters
aliases: [what matters most, prioritize design decisions]
tags: [core-concept, design-philosophy, priorities]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Decide What Matters

Deciding what matters is the meta-principle underlying many design ideas in the book. Structure systems around the things that matter; for things that do not matter, minimize their impact. This principle manifests in [[information-hiding]] (interfaces show what matters to users, implementations hide the rest), [[choosing-names|naming]] (names convey the most important aspects), [[abstractions|abstraction]] (omit only truly unimportant details), and [[designing-for-performance|performance]] (design around the critical path when speed matters).

## Finding Leverage

Look for leverage points where one decision unlocks many others. A general-purpose interface provides more leverage than specialized methods because one abstraction solves many problems. Invariants are leverage points: knowing one rule about a variable or structure predicts behavior across many situations. [[design-it-twice|Designing it twice]] helps identify what matters by forcing you to compare multiple approaches and see which aspects each one emphasizes.

## Minimize What Matters

The fewer things that matter, the simpler the system. Minimize constructor parameters and provide sensible defaults. Hide information within modules so it does not matter to external code. Handle [[exception-handling|exceptions]] at the lowest possible level so they do not propagate. Compute configuration values automatically rather than exposing them as parameters.

## Emphasize and De-emphasize

Important things should be prominent (visible in interfaces, well-named), repeated (key ideas appear throughout), and central (they determine system structure). Unimportant things should be hidden, encountered infrequently, and structurally isolated. Two mistakes are common: treating too many things as important (cluttering the design, creating [[shallow-modules|shallow classes]]) and failing to recognize something as important (leading to [[unknown-unknowns]] and missing functionality).

## Good Taste

"Good taste" describes the ability to distinguish what is important from what is not. This skill applies beyond software: technical writing works best when structured around a few key concepts, and life itself benefits from focusing energy on what matters most. Developing good taste requires practice -- make hypotheses, commit to them, and learn from the results.

## Related
- [[information-hiding]] -- hiding what does not matter to module users
- [[abstractions]] -- interfaces reflect what matters, implementations hide the rest
- [[design-it-twice]] -- comparing options reveals what truly matters
- [[choosing-names]] -- names should convey the aspects that matter most
- [[designing-for-performance]] -- when performance matters, structure around it
- [[shallow-modules]] -- often result from treating too many things as important
- [[a-philosophy-of-software-design-ch21]] -- the source chapter
