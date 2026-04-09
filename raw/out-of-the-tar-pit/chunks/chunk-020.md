# 8.1 Structure

8.1 Structure
8.1.1 Relations
As mentioned above, relations provide the sole means for structuring data
in the relational model. A relation is best seen as a homogeneous set of
records,eachrecorditselfconsistingofaheterogeneoussetofuniquelynamed
attributes (this is slightly di↵erent from the general mathematical definition
of a relation as a set of tuples whose components are identified by position
rather than name).
Implications of this definition include the fact that — by virtue of being
aset—arelationcancontainnoduplicates, andithasnoordering. Bothof
these restrictions are in contrast with the common usage of the word table
which can obviously contain duplicate rows (and column names), and — by
virtue of being a visual entity on a page — inevitably has both an ordering
of its rows and of its columns.
Relations can be of the following kinds:
Base Relations are those which are stored directly
Derived Relations (also known as Views) are those which are defined in
terms of other relations (base or derived) — see section 8.2
Following Date [Dat04] it is useful to think of a relation as being a
single (albeit compound) value, and to consider any mutable state not as a
“mutable relation” but rather as a variable which at any time can contain
a particular relation value. Date calls these variables relation variables or
relvars, leading to the terms base relvar and derived relvar, and we shall
use this terminology later. (Note however that our definition of relation is
slightlydi↵erentfromhisinthat—followingstandardstatictypingpractice
— we do not consider the type to be part of the value).
8.1.2 Structuring benefits of Relations — Access path indepen-
dence
The idea of structuring data using relations is appealing because no subjec-
tive, up-front decisions need to be made about the access paths that will
later be used to query and process the data.
To understand what is meant by access path, let us consider a simple
example. Suppose we are trying to represent information about employees
and the departments in which they work. A system in which choosing the
structure for the data involves setting up “routes” between data instances
38

---
Page 39
---

(such as from a particular employee to a particular department) is access
path dependent.
Thetwomaindatastructuringapproacheswhichprecededtherelational
model (the network and hierarchical models) were both access path depen-
dent in this way. For example, in the hierarchical model a subjective choice
would be forced early on as to whether departments would form the top
level (with each department “containing” its employees) or the other way
round (with employees “containing” their departments). The choice made
would impact all future use of the data. If the first alternative was selected,
then users of the data would find it easy to retrieve all employees within a
given department (following the access path), but they would find it harder
to retrieve the department of a given employee (and would have to use some
other technique corresponding to a search of all departments). If the second
alternative was selected then the problem was simply reversed.
The network model alleviated the problem to some degree by allowing
multiple access paths between data instances (so the choice could be made
to provide both an access path from department to employee and an access
path from employee to department). The problem of course is that it is
impossible to predict in advance what all the future required access paths
will be, and because of this there will always be a disparity between:
Primary retrieval requirements which were foreseen, and can be satis-
fied simply by following the provided access paths
Secondary retrieval requirements which were either unforeseen, or at
least not specially supported, and hence can only be satisfied by some
alternative mechanism such as search
The ability of the relational model to avoid access paths completely was
one of the primary reasons for its success over the network and hierarchical
models.
It is also interesting to consider briefly what is involved when taking an
object-oriented (OOP) approach to our example. We can choose between
the following options:
Give Employee objects a reference to their Department
•
Give Department objects a set (or array) of references to their Em-
•
ployees
Both of the above
•
39

---
Page 40
---

If we choose the third option, then we at best expose ourselves to extra
workinmaintainingtheredundantreferences, andatworstexposeourselves
to bugs.
Therearedisturbingsimilaritiesbetweenthedatastructuringapproaches
of OOP and XML on the one hand and the network and hierarchical models
on the other.
A final advantage of using relations for the structure — in contrast with
approaches such as Chen’s ER-modelling [Che76] — is that no distinction
is made between entities and relationships. (Using such a distinction can be
problematic because whether something is an entity or a relationship can
be a very subjective question).
