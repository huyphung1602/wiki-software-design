---
title: Red Flags
aliases: [code smells, design red flags]
tags: [core-concept, code-review, heuristics]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Red Flags

Red flags are heuristics for recognizing when a piece of code is probably more complicated than it needs to be. Ousterhout introduces this concept as a practical tool for improving design skill: when you see a red flag, stop and look for an alternate design that eliminates the problem.

The book identifies specific red flags throughout its chapters, including:
- **Shallow Module** — interface nearly as complex as implementation (Ch 4)
- **Information Leakage** — same knowledge used in multiple places, such as two classes both understanding a file format (Ch 5)
- **Temporal Decomposition** — execution order reflected in code structure, causing information leakage (Ch 5)
- **Overexposure** — API for a common feature forces users to learn about rarely used features (Ch 5)
- **One-use method** — a method designed for one particular use is likely too special-purpose; replace several special-purpose methods with a single general one (Ch 6)
- **Too-hard API** — if you need lots of extra code to use a class for current needs, the interface doesn't provide the right functionality (Ch 6)
- **Pass-Through Method** — does nothing except pass its arguments to another method with the same API, indicates confused division of responsibility (Ch 7)
- **Repetition** — same code (or nearly the same) appearing over and over means wrong abstractions (Ch 9)
- **Special-General Mixture** — general-purpose mechanism contaminated with code specialized for a particular use (Ch 9)
- **Conjoined Methods** — can't understand one method's implementation without reading another's (Ch 9)
- **Comment Repeats Code** — comment uses same words as code or name, provides no additional information (Ch 13)
- **Implementation Documentation Contaminates Interface** — interface docs describe implementation details users don't need (Ch 13)
- **Vague Name** — variable or method name is broad enough to refer to many different things (Ch 14)
- **Hard to Pick Name** — if it's hard to find a simple name for a variable or method, the underlying object may not have a clean design (Ch 14)
- **Hard to Describe** — if you can't write a simple yet complete comment for a method or variable, the design has problems (Ch 15)
- **Nonobvious Code** — if the meaning and behavior of code cannot be understood with a quick reading, important information is not immediately clear (Ch 18)
- Special cases that complicate logic
- Naming that isn't precise or consistent

The best way to develop an eye for red flags is through **code reviews** — it's easier to spot design problems in someone else's code than your own. Over time, recognizing red flags becomes instinctive, and your designs get cleaner.

## Related
- [[complexity]] — what red flags signal
- [[continuous-design]] — the process where red flags get caught and fixed
- [[a-philosophy-of-software-design-ch01]] — where red flags are introduced as a concept
- [[a-philosophy-of-software-design-ch05]] — where information leakage, temporal decomposition, and overexposure are identified
