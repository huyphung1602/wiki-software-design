---
title: Change Amplification
aliases: [scattered changes, ripple effect]
tags: [symptom, complexity, coupling]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Change Amplification

Change amplification is the first symptom of [[complexity]]: a seemingly simple change requires code modifications in many different places. Ousterhout's example: an early website where the banner background color was hardcoded on every page. Changing the color meant editing thousands of pages individually. The fix — a central variable referenced by all pages — collapsed the change to a single location.

The goal of good design is to reduce the amount of code affected by each design decision. When a design decision is localized, changes are cheap and safe. When it's scattered, changes are expensive and error-prone.

Change amplification is annoying but manageable — as long as it's clear *which* code needs to change. This makes it the least dangerous of the three symptoms of complexity (the worst being [[unknown-unknowns]]).

## Cases
- [[kwic-index-two-decompositions]] — five hypothetical changes tested against both KWIC decompositions; four of five propagate to all modules in the conventional decomposition but stay isolated in the information-hiding decomposition, illustrating how decomposition criterion directly controls change amplification (from Criteria for Modularization)
- [[compiler-team-theory]] — group B's modifications without the theory created patches that destroyed the compiler's structure; each subsequent modification accumulated more decay; the theory-holding team's absence caused change amplification at the structural level (from Programming as Theory Building)

## Related
- [[complexity]] — the problem this symptom signals
- [[dependencies-and-obscurity]] — the root cause (dependencies scatter design decisions)
- [[unknown-unknowns]] — the worse symptom
- [[cognitive-load]] — the other symptom
- [[a-philosophy-of-software-design-ch02]] — where this is defined
