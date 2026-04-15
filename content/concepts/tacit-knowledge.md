---
title: Tacit Knowledge
aliases: [tacit knowledge, implicit knowledge, unarticulated knowledge]
tags: [core-concept, knowledge, programming, documentation]
sources: [naur]
created: 2026-04-15
updated: 2026-04-15
---

# Tacit Knowledge

Tacit knowledge is the knowledge programmers possess that cannot be expressed in documentation or formal rules. Naur draws on Ryle's distinction between knowing how and knowing that: someone with tacit knowledge can do things skillfully and also explain, justify, and answer queries about those activities — but the knowledge itself cannot be reduced to a set of criteria or rules.

The three areas where tacit knowledge necessarily transcends documentation: (1) understanding of how the program maps to the real world and why each part has its particular structure; (2) the ability to justify design decisions, with the final basis always being direct intuitive judgment rather than formal reasoning alone; and (3) the capacity to respond constructively to modification demands by perceiving similarity between new requirements and existing facilities. None of these can be fully articulated — the perception of similarity between situations is a human judgment that no set of rules can capture.

The practical implication: no amount of documentation can substitute for direct contact with programmers who hold the theory. This is why Naur's cases show that even highly motivated teams with complete documentation still fail to grasp design ideas that are immediately obvious to those who built the system. Documentation can jog memories and set up relevant pathways of thought, but it cannot carry the theory itself.

## Cases
- [[compiler-team-theory]] — a compiler team with full documentation and personal advice still could not independently generate the design judgments that the original team made instinctively; demonstrates that theory cannot be transferred by documentation (from Programming as Theory Building)
- [[industrial-monitoring-system]] — 200K LOC industrial monitoring system: programmers with continuous, hands-on involvement could diagnose faults instantly; other teams with formal documentation could not; demonstrates that continuous connection to the system is the only carrier of essential knowledge (from Programming as Theory Building)

## Related
- [[theory-building]] — what the programmer builds
- [[comments-and-documentation]] — documentation's limitations
- [[program-life-death-revival]] — why team continuity matters
- [[naur-ch01]] — where this concept is developed