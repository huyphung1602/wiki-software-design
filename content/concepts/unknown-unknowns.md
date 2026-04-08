---
title: Unknown Unknowns
aliases: [hidden dependencies, unexpected side effects]
tags: [symptom, complexity, risk]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Unknown Unknowns

Unknown unknowns are the worst symptom of [[complexity]]: it is not obvious which pieces of code must be modified to complete a task, or what information a developer must have to carry out the task. There is something you need to know, but no way to find out what it is — or even whether there is an issue. You won't discover it until bugs appear after a change.

Ousterhout's example: a website with a central banner color variable (easy to change), but some pages use a darker shade of that color for emphasis, hardcoded individually. Changing the banner color requires also updating the emphasis color, but nothing makes this obvious. A developer changes the central variable and unknowingly breaks the site's visual consistency.

Why this is the worst symptom:
- **[[change-amplification]]** is annoying, but at least you know what to change
- **[[cognitive-load]]** increases cost, but if you know what to read, you can still get it right
- **Unknown unknowns** mean you don't even know what you're missing

The ideal system is **obvious**: a developer can make a quick guess about what to do and be confident it's correct. This is the opposite of unknown unknowns and high cognitive load.

Well-specified module interfaces help eliminate unknown unknowns. When a module's [[abstractions|interface clearly describes what it does]] and what constraints exist, developers know exactly what they need to use it correctly. The informal aspects of an interface (behavior, constraints) are often where unknown unknowns lurk — they must be documented even though the language cannot enforce them.

## Related
- [[complexity]] — the problem this symptom signals
- [[dependencies-and-obscurity]] — obscurity is what creates unknown unknowns
- [[change-amplification]] — the less dangerous symptom
- [[cognitive-load]] — the other symptom
- [[deep-modules]] — clear interfaces that reduce unknown unknowns
- [[abstractions]] — false abstractions omitting important details create unknown unknowns
- [[a-philosophy-of-software-design-ch02]] — where this is defined
- [[a-philosophy-of-software-design-ch04]] — interfaces as the antidote
