---
title: Wiki Index
tags: [meta]
sources: []
created: 2026-04-08
updated: 2026-04-08
---

# Wiki Index

## Overview
- [[overview]] — High-level synthesis

## Books
- [[a-philosophy-of-software-design]] — Ousterhout, 2021 (23 chapters ingested)
	- [[a-philosophy-of-software-design-preface]] — Preface
	- [[a-philosophy-of-software-design-ch01]] — Ch 1: Introduction
	- [[a-philosophy-of-software-design-ch02]] — Ch 2: The Nature of Complexity
	- [[a-philosophy-of-software-design-ch03]] — Ch 3: Working Code Isn't Enough
	- [[a-philosophy-of-software-design-ch04]] — Ch 4: Modules Should Be Deep
	- [[a-philosophy-of-software-design-ch05]] — Ch 5: Information Hiding (and Leakage)
	- [[a-philosophy-of-software-design-ch06]] — Ch 6: General-Purpose Modules are Deeper
	- [[a-philosophy-of-software-design-ch07]] — Ch 7: Different Layer, Different Abstraction
	- [[a-philosophy-of-software-design-ch08]] — Ch 8: Pull Complexity Downwards
	- [[a-philosophy-of-software-design-ch09]] — Ch 9: Better Together Or Better Apart?
	- [[a-philosophy-of-software-design-ch10]] — Ch 10: Define Errors Out Of Existence
	- [[a-philosophy-of-software-design-ch11]] — Ch 11: Design it Twice
	- [[a-philosophy-of-software-design-ch12]] — Ch 12: Why Write Comments? The Four Excuses
	- [[a-philosophy-of-software-design-ch13]] — Ch 13: Comments Should Describe Things that Aren't Obvious from the Code
	- [[a-philosophy-of-software-design-ch14]] — Ch 14: Choosing Names
	- [[a-philosophy-of-software-design-ch15]] — Ch 15: Write The Comments First
	- [[a-philosophy-of-software-design-ch16]] — Ch 16: Modifying Existing Code
	- [[a-philosophy-of-software-design-ch17]] — Ch 17: Consistency
	- [[a-philosophy-of-software-design-ch18]] — Ch 18: Code Should be Obvious
	- [[a-philosophy-of-software-design-ch19]] — Ch 19: Software Trends
	- [[a-philosophy-of-software-design-ch20]] — Ch 20: Designing for Performance
	- [[a-philosophy-of-software-design-ch21]] — Ch 21: Decide What Matters
	- [[a-philosophy-of-software-design-ch22]] — Ch 22: Conclusion
- [[out-of-the-tar-pit]] — Moseley & Marks, 2006 (12 sections ingested)
	- [[out-of-the-tar-pit-s01]] — S1: Introduction
	- [[out-of-the-tar-pit-s02]] — S2: Complexity
	- [[out-of-the-tar-pit-s03]] — S3: Approaches to Understanding
	- [[out-of-the-tar-pit-s04]] — S4: Causes of Complexity
	- [[out-of-the-tar-pit-s05]] — S5: Classical Approaches to Managing Complexity
	- [[out-of-the-tar-pit-s06]] — S6: Accidents and Essence
	- [[out-of-the-tar-pit-s07]] — S7: Recommended General Approach
	- [[out-of-the-tar-pit-s08]] — S8: The Relational Model
	- [[out-of-the-tar-pit-s09]] — S9: Functional Relational Programming
	- [[out-of-the-tar-pit-s10]] — S10: Example of an FRP System
	- [[out-of-the-tar-pit-s11]] — S11: Related Work
	- [[out-of-the-tar-pit-s12]] — S12: Conclusions

## Concepts
- [[complexity]] — The overarching enemy in software design (2 sources)
- [[problem-decomposition]] — Dividing complex problems into independent pieces (1 source)
- [[strategic-programming]] — Investing in design upfront for long-term system health (2 sources)
- [[tactical-programming]] — Short-term focus on getting features working ASAP (1 source)
- [[modular-design]] — Encapsulating complexity in independent modules (1 source)
- [[continuous-design]] — Design as an ongoing activity, not a phase (1 source)
- [[red-flags]] — Heuristics for spotting overcomplicated code (1 source)
- [[change-amplification]] — Simple change requires many code modifications (1 source)
- [[cognitive-load]] — How much a developer must know to complete a task (1 source)
- [[unknown-unknowns]] — Not obvious what to modify or what info is needed (1 source)
- [[dependencies-and-obscurity]] — The two root causes of complexity (1 source)
- [[tactical-tornado]] — The extreme tactical programmer archetype (1 source)
- [[design-investment]] — Spending 10-20% of dev time on design (1 source)
- [[technical-debt]] — Borrowing time from the future, rarely repaid (1 source)
- [[deep-modules]] — Simple interface, powerful functionality — the ideal module (1 source)
- [[shallow-modules]] — Complex interface relative to functionality — the anti-pattern (1 source)
- [[classitis]] — Cultural bias toward many small classes, producing shallow modules (1 source)
- [[abstractions]] — Simplified views that omit unimportant details (1 source)
- [[information-hiding]] — Encapsulating design decisions within module implementations (1 source)
- [[information-leakage]] — Design decisions reflected in multiple modules (1 source)
- [[temporal-decomposition]] — Structure follows execution order, causing leakage (1 source)
- [[generality]] — Making modules somewhat general-purpose for simpler interfaces (1 source)
- [[specialization]] — Keeping specialized code separate from general-purpose code (1 source)
- [[pass-through-methods]] — Methods that just delegate with same signature (1 source)
- [[pass-through-variables]] — Variables passed through long method chains (1 source)
- [[pull-complexity-downwards]] — Handle complexity internally, keep interfaces simple (1 source)
- [[together-or-apart]] — When to combine or separate functionality (1 source)
- [[exception-handling]] — Reducing complexity from exceptions: define away, mask, aggregate, crash (1 source)
- [[design-it-twice]] — Consider multiple approaches for every major design decision (1 source)
- [[comments-and-documentation]] — Comments as essential for abstraction and managing complexity (1 source)
- [[choosing-names]] — Names should be precise and consistent (1 source)
- [[comments-first-approach]] — Write comments first as a design tool (1 source)
- [[consistency]] — Similar things done in similar ways to reduce complexity (1 source)
- [[obvious-code]] — Code that can be understood with a quick reading (1 source)
- [[designing-for-performance]] — Achieving high performance without sacrificing clean design (2 sources)
- [[decide-what-matters]] — The meta-principle: structure around what matters, hide what does not (1 source)
- [[state-and-complexity]] — Mutable state as the primary cause of software complexity (1 source)
- [[control-flow-complexity]] — Explicit control flow as a cause of complexity (1 source)
- [[essential-complexity]] — Complexity inherent in the problem as seen by users (1 source)
- [[accidental-complexity]] — Complexity from implementation choices that can be eliminated (1 source)
- [[referential-transparency]] — A function always returns the same result for the same arguments (1 source)
- [[functional-relational-programming]] — FRP architecture: functional + relational model with strict separation (1 source)
- [[relational-model]] — Data structuring via relations, algebra, integrity, and data independence (1 source)
- [[declarative-programming]] — Specifying what is required, not how (1 source)
- [[integrity-constraints]] — Declarative, non-interacting rules for data consistency (1 source)
- [[data-independence]] — Separation of logical model from physical storage (1 source)
- [[accidental-state]] — State that can be eliminated or separated from essential logic (1 source)
- [[testing]] — Black-box validation: observing behavior with specific inputs (1 source)
- [[reasoning]] — White-box analysis: understanding code through mental simulation (1 source)

## Comparisons
- [[strategic-vs-tactical-programming]] — Strategic investment vs. tactical shortcuts in software development (1 source)
- [[generality-vs-specialization]] — The trade-off between general-purpose and special-purpose design (1 source)
- [[deep-modules-vs-shallow-modules]] — Principle vs anti-pattern: interface cost vs functionality benefit (1 source)
- [[information-hiding-vs-information-leakage]] — Encapsulating knowledge vs spreading it across modules (1 source)
- [[problem-decomposition-vs-temporal-decomposition]] — Organizing by knowledge boundaries vs execution order (1 source)
- [[designing-for-performance-vs-complexity]] — Why simpler code tends to be faster, and when trade-offs are real (1 source)
- [[essential-vs-accidental-complexity]] — Inherent problem complexity vs eliminable implementation complexity (1 source)
- [[testing-vs-reasoning]] — Black-box validation vs white-box analysis of software correctness (1 source)
