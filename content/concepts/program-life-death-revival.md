---
title: Program Life, Death, and Revival
aliases: [program life cycle, program death, program revival]
tags: [core-concept, programming, theory-building, team]
sources: [naur]
created: 2026-04-15
updated: 2026-04-15
---

# Program Life, Death, and Revival

Program life, death, and revival is Naur's conceptual framework for understanding a program's existence in relation to the human teams that hold its theory. A program is born when its theory is built by the original programmer team. It lives as long as a team possessing that theory remains in active control, retaining authority over all modifications. It dies when that team dissolves — though it may continue executing and producing useful results, it can no longer be intelligently modified. Revival is the attempt to rebuild the theory by a new team, working from documentation alone.

The central claim: program revival is strictly impossible. The theory cannot be reconstructed from artifacts — no matter how complete the documentation, it cannot carry the tacit knowledge that is the theory. The best outcome of an revival attempt is a revived theory that differs from the original, potentially containing discrepancies with the program text. More often, attempting to reverse-engineer a theory from code and documents is so costly and frustrating that the better path is to discard the existing code entirely and solve the problem fresh.

The practical implication for team management: program life depends on maintaining continuity of people who hold the theory. This has implications for hiring, project staffing, and knowledge transfer — any practice that disrupts the continuity of the team holding the theory shortens the program's life.

## Cases
- [[compiler-team-theory]] — compiler case: after original team dispersed, modifications accumulated as amorphous additions destroying the original structure; demonstrates that program death (loss of theory-holding team) cannot be reversed by documentation (from Programming as Theory Building)
- [[industrial-monitoring-system]] — installation programmers who maintained continuous connection to the system could diagnose faults easily; other teams with formal documentation could not; demonstrates that knowledge of the system is bound to continuous personal involvement, not documentation (from Programming as Theory Building)

## Related
- [[theory-building]] — what the program lifecycle is based on
- [[tacit-knowledge]] — why revival is impossible
- [[naur-ch01]] — where this concept is developed