---
title: Theory Building
aliases: [theory building view, programming as theory building]
tags: [core-concept, programming, knowledge, design]
sources: [naur]
created: 2026-04-15
updated: 2026-04-15
---

# Theory Building

Programming as theory building is Naur's central thesis: the primary result of programming is not the program text but the theory that programmers build of how the program maps to the real world. The theory encompasses not just knowing that the program works, but understanding why each design decision was made, how the program relates to the real world activity it supports, and how to extend it to handle new situations.

This view stands in contrast to the production view of programming, which regards programming as making a program and related texts. On the production view, documentation captures the design and the programmer's job is to produce more documentation. On the theory building view, documentation is secondary and auxiliary — it can jog memories and set up pathways of thought, but the theory itself cannot be written down.

The theory includes three kinds of knowledge that necessarily transcend documentation: the programmer knows how the real world maps into the program and why each part has its structure; can justify each design decision with the final basis being intuitive judgment; and can respond constructively to modification demands by perceiving similarity between new requirements and existing facilities. None of these can be reduced to rules — the perception of similarity is a human judgment that cannot be formalized.

Naur's source is Peter Naur's "Programming as Theory Building" (1985).

## Cases
- [[compiler-team-theory]] — compiler case demonstrates that the production view (documentation captures design) is false: group B had full documentation and personal advice but still could not generate design judgments without group A; the theory was held by people, not artifacts (from Programming as Theory Building)

## Related
- [[tacit-knowledge]] — the kind of knowledge that theory comprises
- [[program-life-death-revival]] — the life cycle that follows from this view
- [[continuous-design]] — theory building as ongoing design activity
- [[reasoning]] — intellectual activity as distinct from rules-following
- [[comments-and-documentation]] — documentation as secondary to the theory
- [[naur-ch01]] — where this concept is developed