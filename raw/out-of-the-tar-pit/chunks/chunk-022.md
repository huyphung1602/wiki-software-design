# 8.3 Integrity

8.3 Integrity
Integrity in the relational model is maintained simply by specifying — in a
purely declarative way — a set of constraints which must hold at all times.
Any infrastructure implementing the relational model must ensure that
these constraints always hold — specifically attempts to modify the state
which would result in violation of the constraints must be either rejected
outright or restricted to operate within the bounds of the constraints.
The most common types of constraint are those identifying candidate or
primary keys and foreign keys. Constraints may in fact be arbitrarily com-
plex,involvemultiplerelations,andbeconstructedfromeithertherelational
calculus or the relational algebra.
Finally, many commercially available DBMSs provide imperative mech-
anisms such as triggers for maintaining integrity — such mechanisms su↵er
from control-flow concerns (see section 4.2) and are not considered to be
part of the relational model.
