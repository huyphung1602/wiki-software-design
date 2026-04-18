---
title: "Chapter 7 - Different Layer, Different Abstraction"
tags: [chapter, software-design, modules, layers]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Chapter 7 - Different Layer, Different Abstraction

Part of [[a-philosophy-of-software-design]]

In a well-designed layered system, each layer provides a different [[abstractions|abstraction]] from the layers above and below. If adjacent layers have similar abstractions, that's a [[red-flags|red flag]] indicating a decomposition problem. This principle applies to both interfaces (methods) and implementations (internal representations).

[[pass-through-methods|Pass-through methods]] are the most common symptom: methods that just delegate to another method with the same signature. They add interface complexity without adding functionality. Solutions: expose the lower class directly, redistribute functionality, or merge classes. Exception: dispatchers (same signatures, but the dispatcher provides the useful service of choosing which to call) and multiple interface implementations.

Decorators (wrappers) are a related anti-pattern. They extend an object by wrapping it with the same API, but tend to produce shallow classes with many pass-through methods. The Java I/O library is an example — `BufferedInputStream` wraps `InputStream` with identical API, adding only buffering. Before creating a decorator, consider adding functionality to the underlying class, merging with the use case, or implementing stand-alone.

Interface should differ from implementation. A text class with line-oriented storage but a line-oriented API is shallow — callers must split and join lines themselves. A character-oriented API (`insert` at arbitrary position, `delete` between positions) encapsulates line management inside the class, making it [[deep-modules|deeper]].

[[pass-through-variables|Pass-through variables]] are the variable analogue: values passed through long method chains but only needed at the bottom. They add [[change-amplification]] and cognitive load to every intermediate method. The best available solution is a context object that stores all global state, passed only in constructors.

The underlying principle: every design element (interface, argument, class) adds complexity. It must eliminate more complexity than it introduces, or it's not worth having.

## Related
- [[pass-through-methods]] — the primary pattern this chapter addresses
- [[pass-through-variables]] — the variable form
- [[shallow-modules]] — what similar abstractions across layers produce
- [[deep-modules]] — what different abstractions across layers enable
- [[a-philosophy-of-software-design-ch04]] — deep modules, the foundation
