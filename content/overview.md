---
title: Overview
tags: [meta]
sources: []
created: 2026-04-08
updated: 2026-04-08
---

# Overview

This wiki is a personal knowledge base on software design, built incrementally from book sources.

## Current Sources
- **A Philosophy of Software Design** (Ousterhout, 2021) — complete (23/23 chapters). Argues that reducing [[complexity]] is the primary goal of software design. Core themes: [[problem-decomposition]] as the fundamental skill, [[strategic-programming|strategic programming]] over [[tactical-programming|tactical coding]], [[modular-design]] to encapsulate complexity, [[continuous-design]] as an ongoing practice.
- **Out of the Tar Pit** (Moseley & Marks, 2006) — complete (12/12 sections). Argues that most [[complexity]] is [[accidental-complexity|accidental]], caused by [[state-and-complexity|state]] and [[control-flow-complexity|control flow]]. Proposes [[functional-relational-programming]] as a complexity-eliminating architecture. Core themes: state avoidance, [[declarative-programming]], [[relational-model]] for application design, [[referential-transparency]].

## Emerging Themes
- [[complexity]] is the central antagonist — both sources agree this is the root problem
- [[accidental-complexity|Accidental complexity]] dominates most systems — caused by implementation choices, not inherent problem difficulty
- [[state-and-complexity|State]] is the single biggest cause of complexity — mutable state creates exponential scenarios
- [[control-flow-complexity|Control flow]] is the second major cause — unnecessary ordering specifications
- Complexity defined structurally (Ousterhout): anything making code hard to understand and modify
- Three symptoms: [[change-amplification]], [[cognitive-load]], [[unknown-unknowns]] (the worst)
- Two root causes (Ousterhout): [[dependencies-and-obscurity]] — dependencies scatter decisions, obscurity hides information
- Two strategies: eliminate complexity (simpler code) or encapsulate it ([[modular-design]])
- [[functional-relational-programming|FRP]] proposes a third strategy: architecturally eliminate accidental complexity by separating essential state, essential logic, and accidental components
- [[declarative-programming|Declarative]] over imperative — specify WHAT, not HOW
- [[referential-transparency]] makes testing and reasoning far more effective
- [[relational-model]] provides [[data-independence]] and [[integrity-constraints]] for managing essential state
- [[reasoning|Reasoning]] about code is more important than testing — both degrade with complexity
- Complexity is incremental — accumulates in small pieces, requires zero tolerance
- [[strategic-programming|Strategic programming]] is the answer: invest [[design-investment|10-20% of dev time]] in design
- [[technical-debt|Technical debt]] is rarely repaid — continuous small investments are the only cure
- Design is [[continuous-design|continuous]], not a phase — always be improving
- [[red-flags]] as practical heuristics for catching design problems early
- [[deep-modules]] are the primary structural tool — simple interface, powerful functionality
- [[shallow-modules]] and [[classitis]] are anti-patterns that add interface complexity without hiding proportionally more
- [[abstractions]] must omit only truly unimportant details — false abstractions create obscurity
- [[information-hiding]] is the primary technique for achieving depth — encapsulate design decisions as knowledge
- [[information-leakage]] is the enemy: knowledge reflected in multiple modules creates dependencies
- [[temporal-decomposition]] is a common cause of leakage — design around knowledge, not execution order
- [[generality|Over-specialization]] may be the single greatest cause of complexity — "somewhat general-purpose" is the sweet spot
- Push specialization upward (top-level classes) or downward (device drivers), never let it leak into general-purpose code
- Eliminate special cases — design the normal case to handle edges automatically
- Each layer should provide a different abstraction — pass-through methods and decorators indicate decomposition problems
- [[pull-complexity-downwards|Pull complexity down]] — simple interface matters more than simple implementation; configuration parameters often push complexity up
- [[together-or-apart|Together or apart]] — the fundamental decomposition question; depth matters more than length; over-splitting is worse than long methods
- [[exception-handling|Exception handling]] is a major complexity source — define errors out of existence, mask, aggregate, or crash
- [[design-it-twice|Design it twice]] — consider multiple radically different approaches for every major decision
- [[comments-and-documentation|Comments]] are essential for abstraction — describe what isn't obvious from code, at a different level of detail
- [[choosing-names|Names]] should be precise and consistent — a form of documentation; vague names cause bugs
- [[comments-first-approach|Write comments first]] — they serve as a design tool and a canary for complexity
- The ideal system is "obvious" — a quick guess about what to do is likely correct
- [[consistency|Consistency]] creates cognitive leverage and reduces mistakes across a codebase
- [[obvious-code|Obvious code]] can be understood with a quick reading; nonobviousness is a red flag
- [[designing-for-performance|Performance and clean design]] are allies — simpler code tends to be faster; measure before optimizing
- [[decide-what-matters|Decide what matters]] — the meta-principle: structure around what matters, hide what does not
