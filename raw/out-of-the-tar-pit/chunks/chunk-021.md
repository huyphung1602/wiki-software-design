# 8.2 Manipulation

8.2 Manipulation
Codd introduced two di↵erent mechanisms for expressing the manipulation
aspects of the relational model — the relational calculus and the relational
algebra. They are formally equivalent (in that expressions in each can be
converted into equivalent expressions in the other), and we shall only con-
sider the algebra.
The relational algebra (which is now normally considered in a slightly
di↵erentformfromtheoneusedoriginallybyCodd)consistsofthefollowing
eight operations:
Restrict is a unary operation which allows the selection of a subset of the
records in a relation according to some desired criteria
Project is a unary operation which creates a new relation corresponding
to the old relation with various attributes removed from the records
Product is a binary operation corresponding to the cartesian product of
mathematics
Union isabinaryoperationwhichcreatesarelationconsistingofallrecords
in either argument relation
Intersection is a binary operation which creates a relation consisting of all
records in both argument relations
Di↵erence is a binary operation which creates a relation consisting of all
records in the first but not the second argument relation
40

---
Page 41
---

Join is a binary operation which constructs all possible records that re-
sult from matching identical attributes of the records of the argument
relations
Divide isaternaryoperationwhichreturnsallrecordsofthefirstargument
whichoccurinthesecondargumentassociatedwitheach recordofthe
third argument
One significant benefit of this manipulation language (aside from its
simplicity) is that it has the property of closure — that all operands and
results are of the same kind (relations) — hence the operations can be
nested in arbitrary ways (indeed this property is inherent in any single-
sorted algebra).
