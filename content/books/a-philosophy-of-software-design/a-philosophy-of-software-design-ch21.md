---
title: "Ch 21: Decide What Matters"
tags: [software-design, priorities, design-philosophy]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Ch 21: Decide What Matters

Part of [[a-philosophy-of-software-design]]

[[decide-what-matters|Deciding what matters]] is the meta-principle underlying many of the book's other ideas. Structure systems around the things that matter; for things that do not matter, minimize their impact. Emphasize what matters through prominence, repetition, and centrality; de-emphasize what does not by hiding it.

## Identifying What Matters

Look for leverage: where solving one problem solves many others, or where one piece of information explains many things. A general-purpose interface provides more leverage than specialized methods. Invariants are leverage points -- knowing one rule predicts behavior across many situations. [[design-it-twice|Designing it twice]] applies here: generate multiple options and choose the one that emphasizes the most important aspects. When unsure, make a hypothesis about what matters, commit to it, and learn from the result.

## Minimizing What Matters

Try to make as little matter as possible. Minimize constructor parameters, provide sensible defaults, and hide information within modules. If an exception can be handled entirely at a low level, it does not matter to the rest of the system. If a configuration parameter can be computed automatically, it no longer matters to administrators. Simpler systems result from fewer things that matter.

## Two Kinds of Mistakes

Treating too many things as important clutters the design with unimportant details, adding complexity. The Java I/O interface is an example: it forced developers to think about buffered vs. unbuffered I/O even though this distinction almost never matters. Failing to recognize something as important leads to hidden critical information and missing functionality, creating [[unknown-unknowns]]. "Good taste" in software design is precisely this ability to distinguish what matters from what does not.

## Related
- [[decide-what-matters]] -- the concept page for this chapter's core idea
- [[information-hiding]] -- hiding what does not matter to users of a module
- [[abstractions]] -- interfaces reflect what matters, implementations hide the rest
- [[design-it-twice]] -- evaluating options to find what matters most
- [[choosing-names]] -- names should convey what matters about a variable
- [[designing-for-performance]] -- when performance matters, design around it
