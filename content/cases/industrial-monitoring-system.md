---
title: Industrial Monitoring System
tags: [case, tacit-knowledge, program-life-death-revival, documentation]
concepts: [tacit-knowledge, program-life-death-revival, comments-and-documentation]
sources: [naur]
crossroad: false
created: 2026-04-15
updated: 2026-04-15
---

# Industrial Monitoring System

## The Story

A large real-time system for monitoring industrial production activities was delivered with program sizes on the order of 200,000 lines. Each installation was adapted individually to its specific environment of sensors and display devices. The system's producer employed a dedicated group of installation and fault-finding programmers who had been closely concerned with the system over several years, from initial design through ongoing maintenance.

Two observations about this group stand out. First, when diagnosing faults, these programmers relied almost exclusively on their ready knowledge of the system and the annotated program text. They were unable to name any additional documentation that would have been useful to them. Second, other programmer groups — responsible for operating particular installations and receiving full documentation and guidance from the producer's staff — regularly encountered difficulties that the installation programmers could clear up easily upon consultation.

The conclusion: with certain kinds of large programs, continued adaptation, modification, and error correction are essentially dependent on knowledge possessed by programmers who are closely and continuously connected with the system. Documentation, no matter how complete, cannot substitute for this ongoing, direct contact with the living system.

## Fragments

### Documentation Is Always Behind the Current State
The installation programmers could not identify useful additional documentation because documentation is always behind the current state of the program. Their knowledge was not derived from documentation — it came from continuous, hands-on engagement with the system as it evolved. No document could have captured what they knew, because what they knew was built through years of seeing how the system actually behaved in their specific environment.
Illustrates: [[comments-and-documentation]], [[tacit-knowledge]]

### Continuous Team Connection Is the Carrier of Knowledge
Other programmer groups with formal documentation and producer guidance still encountered difficulties that the installation programmers resolved instantly. The difference was not documentation quality or motivation — it was continuous, direct involvement with the system through its life. This is Naur's central claim about [[tacit-knowledge]]: the knowledge that makes intelligent modification possible cannot be transferred by documentation, only by direct personal contact over time.
Illustrates: [[tacit-knowledge]], [[program-life-death-revival]]

### Large Programs Create Special Knowledge Requirements
At 200,000 lines, the system was large enough that no single document could capture its design rationale. But more importantly, the adaptation to specific sensor and display environments meant each installation was partially unique. The knowledge of how the system mapped to these real-world contexts was built through years of on-site work — knowledge that existed nowhere except in the heads of the installation programmers.
Illustrates: [[theory-building]], [[program-life-death-revival]]

## Related Cases
- [[compiler-team-theory]] — the compiler case makes the same point with a different system: documentation and even annotated code cannot transfer the theory; personal contact is essential

## Source
- [[naur-ch01]] — D.L. Parnas, "Programming as Theory Building," 1985, Case 2