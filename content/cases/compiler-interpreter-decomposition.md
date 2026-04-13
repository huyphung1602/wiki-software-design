---
title: Compiler-Interpreter Decomposition
tags: [case, modular-design, information-hiding, generality]
concepts: [information-hiding, modular-design, generality]
sources: [criteria-for-modularization]
crossroad: false
created: 2026-04-13
updated: 2026-04-13
---

# Compiler-Interpreter Decomposition

## The Story

Parnas's team applied information-hiding decomposition rules to a design project for a Markov algorithm translator. Their goal was not to investigate the relationship between compilers and interpreters — it simply emerged from the decomposition.

A Markov algorithm translator can be implemented as a pure compiler (producing standalone output) or as several varieties of interpreters (executing the algorithm at runtime). These are fundamentally different execution models with radically different runtime representations. Yet when the team applied information-hiding decomposition, they found the same modular structure worked for all variants. Register representation, search algorithm, rule interpretation — each became a module, and these modules were valid across both compiler and interpreter implementations.

This would not have happened with a conventional decomposition. Classical decompositions divide responsibilities along functional lines: syntax recognizer, code generator, runtime routines for a compiler vs. syntax recognizer, interpreter engine, runtime routines for an interpreter. These produce different module structures for each variant, and routines cannot be shared.

The information-hiding decomposition succeeded because it was organized around design decisions — the things that transcend execution model. When a design decision is hidden behind a clean interface, the module works regardless of whether that decision results in compiled machine code or interpreted execution.

## Fragments

### Design Decisions Transcend Execution Model
Register allocation strategy, rule interpretation mechanism, and search algorithm are all design decisions that exist in both compilers and interpreters. In a conventional decomposition, these decisions are buried inside modules named after execution phases (code generator, interpreter engine) — phases that don't exist in both variants. In information hiding, these become independent modules valid across all implementations.
Illustrates: [[information-hiding]], [[modular-design]]

### Decomposition Reuse Across Related Problems
The same module structure worked for a pure compiler and multiple interpreter variants. Routines could be reused with only slight changes across all translator types. This demonstrates that information hiding produces decompositions that are robust across related problem domains — not just across hypothetical changes within a single system, but across genuinely different system types sharing the same problem space.
Illustrates: [[generality]]

### Independence From Processing Order
The decomposition was not organized around when things happen (parsing phase, code generation phase, runtime phase) but around what design decisions exist. This is why it survived the transition between compiler and interpreter — those processing phases are different, but the underlying design decisions are the same. The order in which processing occurs should not drive decomposition.
Illustrates: [[information-hiding]], [[temporal-decomposition]]

## Related Cases
- [[kwic-index-two-decompositions]] — demonstrates the same principle with a simpler, more detailed example

## Source
- [[criteria-for-modularization-ch01]] — D.L. Parnas, 1972, Section 6