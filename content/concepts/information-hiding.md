---
title: Information Hiding
aliases: [encapsulation, data hiding, information encapsulation, information hiding]
tags: [core-concept, modules, design, encapsulation]
sources: [a-philosophy-of-software-design, criteria-for-modularization]
created: 2026-04-08
updated: 2026-04-13
---

# Information Hiding

## In A Philosophy of Software Design

Information hiding is the primary technique for achieving [[deep-modules]]. First described by David Parnas (1972), the idea is that each module should encapsulate a few pieces of knowledge — design decisions — in its implementation, keeping them out of its interface and invisible to other modules.

Hidden knowledge typically includes data structures, algorithms, lower-level details (page sizes), and higher-level assumptions ("most files are small"). Information hiding reduces [[complexity]] in two ways:

1. **Simpler interfaces** — The interface reflects a simpler, more abstract view, reducing [[cognitive-load]] on developers using the module. A developer using a B-tree class need not worry about fanout or rebalancing.
2. **Easier evolution** — If information is hidden, there are no dependencies on it outside the module. Changes affect only one module. If TCP changes its congestion control, higher-level code using TCP should not need modification.

**Private ≠ hidden.** Declaring fields private is not the same as information hiding. If public getters and setters expose the nature and usage of a variable, the information is just as exposed as if the variable were public. The best form of hiding is when information is totally invisible and irrelevant to module users.

**Partial information hiding** also has value. If a feature is only needed by a few of a class's users and accessed through separate methods (so it isn't visible in the most common use cases), that information is mostly hidden and creates fewer dependencies.

Information hiding can be applied at multiple levels — not just between classes, but within a class. Private methods should each encapsulate some information, and the number of places where each instance variable is used should be minimized.

The technique has limits: don't hide information that is needed outside the module. If performance tuning requires configuration, expose it. The goal is to *minimize* information needed outside, not to hide everything.

[[generality|General-purpose interfaces]] improve information hiding. A special-purpose interface tied to current use cases leaks details about those uses into the module (e.g., a `backspace()` method in a text class leaks UI knowledge). A general-purpose interface (`delete(Position, Position)`) keeps the module unaware of higher-level concerns, enabling better separation and more hidden information.

## In Criteria for Modularization

Parnas introduced information hiding in his 1972 paper as the correct criterion for decomposing systems into modules. Against the conventional approach (decompose by processing steps, like a flowchart), Parnas proposed instead that one begins with a list of difficult design decisions or decisions likely to change. Each module is then designed to hide such a decision from all others.

The KWIC index case study demonstrates the difference: in a conventional decomposition, five plausible changes (input format, storage strategy, character packing format, index strategy, alphabetization timing) each propagate to every module. In an information-hiding decomposition, the same changes stay isolated within single modules.

Parnas identified **five specific decomposition guidelines**: (1) data structures and their accessing/modifying procedures belong in the same module; (2) calling sequences and the routines they invoke belong together; (3) control block formats must be hidden; (4) character codes and alphabetic orderings should be hidden; (5) processing sequences should be hidden within a single module.

A subtle but important point: even when applying information hiding correctly, interfaces can still reveal too much. Parnas notes that specifying an ordered list of circular shifts (rather than just specifying that all shifts exist and are unique) unnecessarily restricted the implementation class — a design error.

## Synthesis

Both Parnas (1972) and Ousterhout (2018) agree on the core insight: modules should hide design decisions. They differ in emphasis — Parnas focuses on decisions likely to *change* as the primary decomposition driver; Ousterhout extends this to hiding *any* design decision, including algorithmic complexity and internal design. The KWIC example shows Parnas was particularly attentive to what information is *unnecessarily* exposed in interfaces, not just what is hidden. Both agree that private fields alone do not constitute information hiding if accessor patterns reveal the same information.

## Cases
- [[kwic-index-two-decompositions]] — KWIC index decomposed two ways: by processing steps (bad) vs. design decisions (good); demonstrates how the right criterion contains change propagation (from Criteria for Modularization)
- [[compiler-interpreter-decomposition]] — information-hiding decomposition of a Markov translator was valid across both compiler and interpreter variants, showing design decisions transcend execution model (from Criteria for Modularization)

- [[information-hiding-vs-designing-for-performance]] — Parnas shows that naive information hiding (procedure calls across module boundaries) can hurt performance; recovering performance requires departing from conventional subroutine model and using code injection

## Related
- [[deep-modules]] — what information hiding produces
- [[information-leakage]] — the anti-pattern, the opposite
- [[modular-design]] — the framework this technique supports
- [[complexity]] — what information hiding reduces
- [[criteria-for-modularization-ch01]] — Parnas's original 1972 paper
- [[a-philosophy-of-software-design-ch05]] — where this technique is developed in APSD
- [[a-philosophy-of-software-design-ch19]] — OOP mechanisms support information hiding when used correctly
- [[decide-what-matters]] — hiding what does not matter to module users
- [[obvious-code]] — obvious code reduces information readers need
- [[information-hiding-vs-information-leakage]] — comparison with the anti-pattern