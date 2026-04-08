---
title: Continuous Design
aliases: [continuous design improvement, incremental design]
tags: [core-concept, design-process, methodology]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Continuous Design

Software design is not a phase — it is a continuous process spanning the entire lifecycle of a software system. This distinguishes software from physical engineering (buildings, bridges) where design is largely completed before construction begins.

The waterfall model fails for software because large systems are too complex to visualize completely upfront. Problems with the initial design don't surface until implementation is underway. Incremental approaches (agile, iterative development) work because software is malleable enough to accommodate significant design changes mid-project.

Implications for developers:
- Always be thinking about design issues, not just making features work
- Plan to spend a fraction of your time on design improvements
- The initial design for any component is almost never the best one — expect to redesign
- Each iteration exposes design problems that can be fixed while the system is still small

## Related
- [[complexity]] — what continuous design aims to manage over time
- [[strategic-programming]] — the mindset that makes continuous design possible
- [[a-philosophy-of-software-design-ch01]] — where continuous design is introduced
- [[a-philosophy-of-software-design-ch16]] — applying continuous design when modifying existing code
