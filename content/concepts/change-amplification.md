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

## Related
- [[complexity]] — the problem this symptom signals
- [[dependencies-and-obscurity]] — the root cause (dependencies scatter design decisions)
- [[unknown-unknowns]] — the worse symptom
- [[cognitive-load]] — the other symptom
- [[a-philosophy-of-software-design-ch02]] — where this is defined
