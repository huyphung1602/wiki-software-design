---
title: "S6: Accidents and Essence"
tags: [complexity, essential-complexity, accidental-complexity]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# S6: Accidents and Essence

Building on Brooks' distinction, the authors define [[essential-vs-accidental-complexity]] with a stricter definition of "essential." Essential complexity is inherent in the problem as seen by the users; accidental complexity is everything else -- arising from performance issues, suboptimal languages, and infrastructure. Crucially, bits, bytes, transistors, and even computers themselves are not essential, because they have nothing to do with the users' problem.

The test for essential complexity is strict: if there is any possible way the team could produce a correct system without being concerned with a given type of complexity, that complexity is not essential. In the ideal world, the team would express only the users' problem directly, using general-purpose language and infrastructure, without adding anything else.

Brooks asserted that "the complexity of software is an essential property, not an accidental one," implying that most complexity in large systems is essential. Moseley and Marks disagree. Complexity is not an inherent property of software -- it is perfectly possible to write simple software -- and much of the complexity we observe is not essential to the problem.

This disagreement has profound implications. If Brooks is right, we can only manage complexity; if Moseley and Marks are right, we can eliminate much of it. Their position is that the goal of software engineering must be to eliminate as much accidental complexity as possible and to assist with the truly essential remainder.

The classification sets up the recommendations in section 7: by carefully separating what is essential from what is accidental, and by structuring systems so that accidental concerns cannot contaminate essential ones, we can approach the simplicity of the ideal world even in real systems.

Part of [[out-of-the-tar-pit]]

## Related
- [[essential-vs-accidental-complexity]] — the refined distinction at the heart of the paper
- [[complexity]] — the overarching problem
- [[technical-debt]] — related concept: accumulated accidental complexity
- [[out-of-the-tar-pit-s05]] — Classical Approaches
- [[out-of-the-tar-pit-s07]] — Recommended General Approach
