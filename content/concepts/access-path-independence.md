---
title: Access Path Independence
aliases: [navigational data models, network model, hierarchical model]
tags: [core-concept, data-modeling, relational-model, software-design]
sources: [out-of-the-tar-pit]
created: 2026-04-09
updated: 2026-04-09
---

# Access Path Independence

Access path independence is the property of the [[relational-model]] that there are no predefined routes between data — any relation can be joined with any other on any condition. The query optimizer chooses how to execute the join; the developer does not need to specify.

## The Problem with Navigational Models

In hierarchical and network data models, relationships between records are expressed through access paths — pointers or traversal routes baked into the structure. To find a customer's orders, you follow the path: Customer → Orders. If you also need the customer's region, you may need a different path. The access path is determined when the schema is designed, not when the query is written.

This creates a fundamental mismatch: it is impossible to anticipate all future query patterns. Secondary retrieval requirements — those not foreseen at design time — cannot be satisfied by following access paths. They require search.

The relational model eliminates this problem entirely. Because relations have no inherent navigation, any relationship between data can be queried ad-hoc:

```sql
SELECT c.name, r.region, o.total
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN regions r ON c.region_id = r.id
WHERE o.total > 1000
```

The path from customer to region to order is determined by the query, not the schema. This is what makes the relational model [[data-independence|data-independent]] at the data structure level.

## Connection to Essential vs Accidental Complexity

Moseley and Marks identify access path dependence as an example of [[accidental-complexity]] — complexity that arises from implementation choices rather than the problem itself. The relational model avoids it by choosing a data model where access paths are never baked in.

The same principle applies at the application level: object-oriented models that use references between objects suffer from a form of access path dependence. Choosing whether an `Employee` object references its `Department` or vice versa is a subjective decision that constrains future queries.

## Related

- [[relational-model]] — the model that provides access path independence
- [[data-independence]] — the broader principle that includes access path independence
- [[accidental-complexity]] — access path dependence as an example of accidental complexity
