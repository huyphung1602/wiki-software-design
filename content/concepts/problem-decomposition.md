---
title: Problem Decomposition
aliases: [modular decomposition, system decomposition]
tags: [core-concept, design, decomposition]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Problem Decomposition

Problem decomposition is the most fundamental problem in computer science: how to take a complex problem and divide it into pieces that can be solved independently. Ousterhout calls this the central design task programmers face every day.

Despite its importance, problem decomposition is almost never taught in universities. We teach loops, object-oriented programming, and algorithms — but not how to decompose problems. The state of the art has barely progressed since David Parnas' 1972 paper "On the Criteria to be used in Decomposing Systems into Modules."

The book's design principles — deep modules, information hiding, separating general from special-purpose code — are all techniques for better problem decomposition.

## Related
- [[complexity]] — what problem decomposition aims to manage
- [[a-philosophy-of-software-design]] — the book centered on this idea
- [[problem-decomposition-vs-temporal-decomposition]] — comparison with the seductive anti-pattern
