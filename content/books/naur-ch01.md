---
title: "Naur: Theory Building View"
sources: [naur]
tags: [book, theory-building, tacit-knowledge, programming]
created: 2026-04-15
updated: 2026-04-15
---

# Naur: Theory Building View

Naur opens with a provocation: the dominant view of programming as text production is misleading. Programming properly should be regarded as an activity by which programmers form a theory of how the matters at hand are to be handled by a computer program. The program text is a secondary product; the primary result is the knowledge held by programmers.

**Ryle's notion of theory** grounds this claim. Ryle distinguishes intellectual activity (which requires having a theory) from merely intelligent behavior (which follows rules). The crucial point: if intelligence required following rules, you'd need rules for following rules, ad infinitum — an absurd regress. Having a theory means knowing how to do things and being able to explain, justify, and answer queries about those activities. Crucially, the knowledge that constitutes a theory cannot be expressed in criteria — you cannot capture in rules what makes two situations similar enough to apply the same solution.

**The three transcendent areas.** The programmer's knowledge transcends documentation in three ways: first, knowing how the program maps to the real world — which aspects of the world are relevant, how they map to code, and why the structure is what it is. Second, being able to justify why each part is what it is — with the final basis always being the programmer's direct intuitive knowledge, not formal reasoning alone. Third, responding constructively to modification demands — perceiving similarity between new requirements and existing facilities, which cannot be reduced to rules.

**Two cases** from real experience illustrate: a compiler team with full documentation and personal advice still failed to grasp the deeper design ideas, producing patches that destroyed the original structure. An industrial monitoring system (200K lines) could only be maintained by programmers who had been continuously connected to it — others with documentation still struggled. Both cases show that documentation is insufficient as a carrier of the most important design knowledge.

**Program modifications** reveal the Theory Building View's value. The expectation that modifications should be cheap — because code is easy to edit — assumes programming is text manipulation. On the Theory Building View, this is false. Modifications require perceiving similarity between old and new demands, a judgment only available to those with the theory. When modifications are made by programmers without the theory, the result is amorphous additions that destroy structure. For a program to retain quality, each modification must be grounded in the theory.

**Program life, death, and revival.** A program lives while a team possessing its theory remains in active control. Death occurs when that team dissolves — a dead program may still run but cannot be intelligently modified. Revival (rebuilding the theory from documentation) is strictly impossible on this view, or at best costly and likely to produce a different theory than the original. The recommendation: prefer discarding the code and solving the problem fresh over attempting to reverse-engineer the theory from artifacts.

Part of [[naur]]

## Related
- [[theory-building]] — the core thesis of this chapter
- [[tacit-knowledge]] — the kind of knowledge that cannot be expressed in documentation
- [[program-life-death-revival]] — the life cycle Naur proposes
- [[comments-and-documentation]] — documentation is secondary and auxiliary to the theory
- [[continuous-design]] — the ongoing nature of theory building during programming
- [[reasoning]] — intellectual activity as distinct from rules-following