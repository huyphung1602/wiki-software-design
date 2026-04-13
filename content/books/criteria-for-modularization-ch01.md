---
title: "Criteria for Modularization: Introduction"
sources: [criteria-for-modularization]
tags: [book, modular-design, information-hiding]
created: 2026-04-13
updated: 2026-04-13
---

# Criteria for Modularization: Introduction

D.L. Parnas's 1972 paper presents a deceptively simple idea that reshaped software engineering: the criteria used to decompose a system into modules matters more than the act of modularizing itself. Most programmers instinctively divide systems by processing steps — input, then processing, then output — because that is how flowcharts work. Parnas argues this is almost always wrong.

**The Core Problem with Flowchart-Based Decomposition.** When you decompose by processing steps, the design decisions that govern how the system works — data formats, storage strategies, character encodings, sequencing assumptions — become shared knowledge across modules. Change one of those decisions, and you must update every module that depends on it. The KWIC index example makes this vivid: five plausible changes (input format, character packing, storage location, index strategy, alphabetization timing) each propagate to every module in a conventional decomposition, but stay isolated in an information-hiding decomposition.

**Information Hiding as the Right Criterion.** Parnas proposes instead that one begins with a list of difficult design decisions or decisions likely to change. Each module is then designed to hide such a decision from all others. In the second KWIC decomposition, the line storage module knows everything about data structures; the circular shifter knows nothing about how shifts are computed. The interface of each module is defined to reveal as little as possible about its inner workings. This makes independent development practical: abstract interfaces (function names, parameter types) are simpler decisions than the table formats and data layout of conventional decompositions, allowing teams to begin work earlier and with less coordination.

**The Five Specific Decomposition Guidelines.** Beyond the general principle, Parnas offers concrete rules: (1) data structures and their accessing procedures belong in the same module; (2) calling sequences and the routines they invoke belong together; (3) control block formats in operating systems must be hidden; (4) character codes and alphabetic orderings should be hidden; (5) processing sequences should be hidden within a single module.

**An Efficiency Tradeoff.** Information hiding, implemented naively with procedure calls, can hurt performance — frequent module switching creates calling overhead. Parnas acknowledges this and sketches a solution: implement modules by injecting code where needed rather than through conventional subroutine calls, preserving the abstraction while recovering performance.

**The Compiler/Interpreter Example.** A decomposition based on information hiding, applied to a Markov algorithm translator, turned out to be valid across both compilers and interpreters for the same language. Classical decompositions (syntax recognizer, code generator, runtime) would have been different for each. This demonstrates that information hiding produces decompositions that are robust across related problem domains — a form of design reuse.

**Hierarchical Structure.** The information-hiding decomposition naturally produces a partial ordering: some modules use others without being used themselves. This "uses" relation creates a hierarchy that can be "pruned" — lower-level modules can be reused in other systems while upper levels can be replaced. Importantly, hierarchical structure and clean decomposition are independent properties: you can have one without the other.

The conclusion is stark: it is almost always incorrect to begin decomposition on the basis of a flowchart. The right starting point is a list of design decisions likely to change. Modules will not correspond to steps in the processing — they will cut across time and phase, organized by what might vary.

Part of [[criteria-for-modularization]]

## Related
- [[information-hiding]] — the core criterion introduced by this paper
- [[modular-design]] — the broader discipline this paper established
- [[deep-modules]] — the design ideal that information hiding produces
- [[temporal-decomposition]] — the wrong approach (decompose by processing steps) this paper critiques
- [[change-amplification]] — a complexity symptom that better decomposition reduces