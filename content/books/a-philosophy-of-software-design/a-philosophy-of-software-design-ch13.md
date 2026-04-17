---
title: "Ch 13: Comments Should Describe Things that Aren't Obvious from the Code"
tags: [chapter, software-design, documentation]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Ch 13: Comments Should Describe Things that Aren't Obvious from the Code

Part of [[a-philosophy-of-software-design]]

The guiding principle for [[comments-and-documentation|comments]]: describe things that aren't obvious from the code. Comments should operate at a different level of detail than the code — either more precise (lower-level) or more abstract (higher-level). Comments at the same level as the code just repeat it.

**Don't repeat the code.** If someone could write the comment just by looking at the adjacent code, it has no value. Use different words than the entity's name. Focus on what the entity means, not just what its name says.

**Lower-level comments add precision:** units, boundary conditions (inclusive/exclusive), null meaning, resource ownership, invariants. For variables, describe *what* they represent (nouns), not how they're manipulated (verbs).

**Higher-level comments enhance intuition:** overall intent, why code exists, the one simple idea explaining a block of code. "Try to append the current key hash onto an existing RPC" explains more than narrating each condition in a loop.

**Interface comments define abstractions** and must be separate from implementation comments. If interface comments must describe implementation, the class is shallow — a design clue. Method interface comments: overall behavior, arguments/return values precisely, side effects, exceptions, preconditions.

**Implementation comments** explain what and why, not how. Comment major blocks in longer methods at a higher level. Describe loop purpose abstractly.

**Cross-module design decisions** are the hardest to document. Use a central `designNotes` file with sections, referenced from code with short pointers like `// See "Zombies" in designNotes.`

## Related
- [[comments-and-documentation]] — the comprehensive concept
- [[abstractions]] — what interface comments define
- [[red-flags]] — comment repeats code, implementation docs contaminate interface
- [[a-philosophy-of-software-design-ch12]] — why comments matter
