---
title: "Out of the Tar Pit — S12: Conclusions"
tags: [complexity, simplicity, separation, state, frp]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Out of the Tar Pit — S12: Conclusions

The authors restate their central thesis: [[complexity]] causes more problems in large software systems than anything else, and it can be tamed -- but only through concerted effort to avoid it where possible and separate it where not. A system should be separated into three main parts: essential state, essential logic, and accidental state and control.

Applying these principles at the top level of system design -- effectively using different specialized languages for different components -- offers more simplicity than the unstructured adoption of any single general language, whether imperative, functional, or logic. The authors surveyed each paradigm and highlighted the particular weaknesses of object-orientation as an imperative approach: its reliance on mutable state, the complications of object identity, and its failure to separate concerns.

For existing large systems where [[functional-relational-programming]] cannot be directly applied, the authors recommend focusing on avoiding state, avoiding explicit control where possible, and striving at all costs to reduce code volume. These are pragmatic guidelines that move toward the same principles even without full FRP adoption.

The paper ends with its most memorable statement: "So, what is the way out of the tar pit? What is the silver bullet? ...it may not be FRP, but we believe there can be no doubt that it is simplicity." The specific architecture may vary, but the fundamental strategy -- avoid accidental complexity, rigorously separate what remains -- is the path forward.

This conclusion reinforces Ousterhout's emphasis on [[strategic-programming]] and [[continuous-design]], though from a different angle. Where Ousterhout focuses on managing complexity through good module design, Moseley and Marks argue for eliminating entire categories of complexity by changing how we structure programs.

Part of [[out-of-the-tar-pit]]

## Related
- [[complexity]] — the root cause
- [[functional-relational-programming]] — the proposed path out
- [[strategic-programming]] — Ousterhout's complementary approach
- [[continuous-design]] — ongoing attention to design quality
- [[out-of-the-tar-pit-s07]] — Recommended General Approach
- [[out-of-the-tar-pit-s09]] — Functional Relational Programming
