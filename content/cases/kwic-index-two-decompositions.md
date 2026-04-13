---
title: KWIC Index — Two Decompositions
tags: [case, modular-design, information-hiding, change-amplification]
concepts: [information-hiding, change-amplification, temporal-decomposition, modular-design, deep-modules]
sources: [criteria-for-modularization]
crossroad: false
created: 2026-04-13
updated: 2026-04-13
---

# KWIC Index — Two Decompositions

## The Story

The KWIC index system accepts an ordered set of lines; each line is an ordered set of words; each word is an ordered set of characters. Any line may be circularly shifted by removing the first word and appending it at the end. The system outputs a listing of all circular shifts of all lines in alphabetical order.

Parnas demonstrates that the same system can be decomposed in two radically different ways, with dramatically different changeability properties. Both decompositions work and could produce identical running code — the difference lies entirely in how the system is divided into modules.

**Decomposition 1 (Conventional):** Modules correspond to major processing steps — Input, Circular Shift, Alphabetize, Output, Master Control. This follows the flowchart reflex: identify the steps in processing, assign each to a module. The interfaces are the complex table formats and data layout decisions.

**Decomposition 2 (Information Hiding):** Modules are defined around design decisions. Module 1 (Line Storage) hides the data structure. Module 2 (Circular Shifter) hides the computation method for shifts. Module 3 (Alphabetizer) hides when alphabetization happens. Each module knows only the design decision it is responsible for; nothing about storage format, character packing, or indexing strategy leaks across module boundaries.

Parnas then asks: what happens if five plausible changes are needed? (1) Input format changes; (2) Lines stored on disk instead of core; (3) Characters packed differently; (4) Index computed on-demand instead of pre-built; (5) Alphabetization done lazily instead of upfront. In Decomposition 1, changes 2–5 all propagate to every module. In Decomposition 2, each change stays confined to a single module. The same running code, the same functional result — but radically different maintenance properties.

## Fragments

### The Flowchart Reflex
Decomposition 1 is what most programmers would naturally propose: identify the processing steps (input, circular shift, alphabetize, output), make each a module. This is the flowchart-based decomposition Ousterhout later calls [[temporal-decomposition]]. The problem is that design decisions governing data representation, storage strategy, and sequencing are shared across all modules. Change one decision, update every module.
Illustrates: [[temporal-decomposition]], [[modular-design]]

### Information Hiding in Practice
Decomposition 2's Line Storage module exposes only abstract functions (CHAR, SETCHAR, WORDS, DELINE, DELWRD). The data structure is entirely hidden. The Circular Shifter module has no knowledge of whether shifts are pre-computed or computed on-demand. These are design decisions the module hides. The interfaces are function names and parameter types — abstract enough that independent development can begin before any table layout is finalized.
Illustrates: [[information-hiding]], [[deep-modules]]

### Change Amplification
Five changes tested against both decompositions. In Decomposition 1, four of the five changes ripple through every module. In Decomposition 2, all five changes are confined to the module owning the relevant decision. This is [[change-amplification]] made concrete — the same change request, the same system, and the only variable is the decomposition criterion.
Illustrates: [[change-amplification]]

### Interfaces Reveal Too Much
Even when decomposition 2 is applied correctly, the Circular Shifter module still reveals more than necessary. Parnas notes that specifying the order of circular shifts (lexicographic) was a design error — it restricted implementations to only those where shifts are pre-computed and ordered. A truly general interface would specify only that all shifts exist, no shift appears twice, and the original line is identifiable. The interface itself constrains the design space.
Illustrates: [[information-hiding]], [[modular-design]]

## Related Cases
- [[estate-agency-frp]] — another case demonstrating the difference between good and poor decomposition decisions

## Source
- [[criteria-for-modularization-ch01]] — D.L. Parnas, 1972, Section 2–4