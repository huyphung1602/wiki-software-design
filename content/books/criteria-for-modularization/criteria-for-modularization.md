---
title: 0 - Overview
sources:
  - criteria-for-modularization
created: 2026-04-13
updated: 2026-04-13
---

# Overview

On the Criteria To Be Used in Decomposing Systems into Modules (1972) by D.L. Parnas is one of the foundational papers in software engineering. It transformed how practitioners think about [[modular-design]] by demonstrating that *how* you decompose a system matters far more than the act of decomposing it itself.

The paper introduces the **information hiding** criterion: each module should be defined around a design decision that is likely to change, hiding that decision from all other modules. This contrasts with the conventional approach (decompose by processing steps/flowchart), where changes to implementation details propagate across many modules.

A central contribution is the KWIC index case study, which demonstrates two decompositions of the same problem with radically different changeability properties. The paper also establishes that **hierarchical structure** (modules ordered by "uses"/"depends upon" relations) and **clean decomposition** are independent, desirable properties.

**Key concepts**: [[information-hiding]], [[modular-design]], hierarchical structure, change amplification

## Chapters
- [[criteria-for-modularization-ch01]] — Introduction