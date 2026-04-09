# 5 Classical Approaches

5 Classical approaches to managing complexity
The di↵erent classical approaches to managing complexity can perhaps best
beunderstoodbylookingathowprogramminglanguagesofeachofthethree
major styles (imperative, functional, logic) approach the issue. (We take
object-oriented languages as a commonly used example of the imperative
style).
5.1 Object-Orientation
Object-orientation — whilst being a very broadly applied term (encom-
passing everything from Java-style class-based to Self-style prototype-based
languages, from single-dispatch to CLOS-style multiple dispatch languages,
and from traditional passive objects to the active / actor styles) — is essen-
tially an imperative approach to programming. It has evolved as the domi-
nantmethodofgeneralsoftwaredevelopmentfortraditional(von-Neumann)
computers, and many of its characteristics spring from a desire to facilitate
von-Neumann style (i.e. state-based) computation.
5.1.1 State
In most forms of object-oriented programming (OOP) an object is seen as
consisting of some state together with a set of procedures for accessing and
manipulating that state.
12

---
Page 13
---

This is essentially similar to the (earlier) idea of an abstract data type
(ADT) and is one of the primary strengths of the OOP approach when
compared with less structured imperative styles. In the OOP context this
is referred to as the idea of encapsulation, and it allows the programmer to
enforce integrity constraints over an object’s state by regulating access to
that state through the access procedures (“methods”).
One problem with this is that, if several of the access procedures ac-
cess or manipulate the same bit of state, then there may be several places
where a given constraint must be enforced (these di↵erent access procedures
may or may not be within the same file depending on the specific language
and whether features, such as inheritance, are in use). Another major prob-
lem4 isthatencapsulation-basedintegrityconstraintenforcementisstrongly
biased toward single-object constraints and it is awkward to enforce more
complicated constraints involving multiple objects with this approach (for
one thing it becomes unclear where such multiple-object constraints should
reside).
Identity and State
There is one other intrinsic aspect of OOP which is intimately bound up
with the issue of state, and that is the concept of object identity.
In OOP, each object is seen as being a uniquely identifiable entity re-
gardless of its attributes. This is known as intensional identity (in contrast
with extensional identity in which things are considered the same if their
attributes are the same). As Baker observed [Bak93]:
In a sense, object identity can be considered to be a rejection of
the “relational algebra” view of the world in which two objects
can only be distinguished through di↵ering attributes.
Object identity does make sense when objects are used to provide a
(mutable) stateful abstraction — because two distinct stateful objects can
be mutated to contain di↵erent state even if their attributes (the contained
state) happen initially to be the same.
However, inothersituationswheremutabilityisnot required(suchas—
say — the need to represent a simple numeric value), the OOP approach is
forced to adopt techniques such as the creation of “Value Objects”, and an
4this particular problem doesn’t really apply to object-oriented languages (such as
CLOS) which are based upon generic functions — but they don’t have the same concept
of encapsulation.
13

---
Page 14
---

attempt is made to de-emphasise the original intensional concept of object
identity and re-introduce extensional identity. In these cases it is common
to start using custom access procedures (methods) to determine whether
two objects are equivalent in some other, domain-specific sense. (One risk
— aside from the extra code volume required to support this — is that
there can no longer be any guarantee that such domain-specific equivalence
concepts conform to the standard idea of an equivalence relation — for
example there is not necessarily any guarantee of transitivity).
The intrinsic concept of object identity stems directly from the use of
state,andis(beingpartoftheparadigmitself)unavoidable. Thisadditional
concept of identity adds complexity to the task of reasoning about systems
developed in the OOP style (it is necessary to switch mentally between the
twoequivalenceconcepts—seriouserrorscanresultfromconfusionbetween
the two).
State in OOP
The bottom line is that all forms of OOP rely on state (contained within
objects) and in general all behaviour is a↵ected by this state. As a result
of this, OOP su↵ers directly from the problems associated with state de-
scribed above, and as such we believe that it does not provide an adequate
foundation for avoiding complexity.
5.1.2 Control
Most OOP languages o↵er standard sequential control flow, and many o↵er
explicit classical “shared-state concurrency” mechanisms together with all
thestandardcomplexityproblemsthatthesecancause. Oneslightvariation
isthatactor-stylelanguagesusethe“message-passing”modelofconcurrency
— they associate threads of control with individual objects and messages
arepassedbetweenthese. Thiscanleadtoeasierinformalreasoninginsome
cases, but the use of actor-style languages is not widespread.
5.1.3 Summary — OOP
Conventional imperative and object-oriented programs su↵er greatly from
both state-derived and control-derived complexity.
14

---
Page 15
---

5.2 Functional Programming
Whilst OOP developed out of a desire to o↵er improved ways of managing
and dealing with the classic stateful von-Neumann architecture, functional
programming has its roots in the completely stateless lambda calculus of
Church (we are ignoring the even simpler functional systems based on com-
binatory logic). The untyped lambda calculus is known to be equivalent
in power to the standard stateful abstraction of computation — the Turing
machine.
5.2.1 State
Modern functional programming languages are often classified as ‘pure’ —
those such as Haskell[PJ+03] which shun state and side-e↵ects completely,
and ‘impure’ — those such as ML which, whilst advocating the avoidance of
state and side-e↵ects in general, do permit their use. Where not explicitly
mentioned we shall generally be considering functional programming in its
pure form.
The primary strength of functional programming is that by avoiding
state (and side-e↵ects) the entire system gains the property of referential
transparency — which implies that when supplied with a given set of argu-
mentsafunctionwillalways returnexactlythesameresult(speakingloosely
we could say that it will always behave in the same way). Everything which
can possibly a↵ect the result in any way is always immediately visible in the
actual parameters.
It is this cast iron guarantee of referential transparency that obliterates
one of the two crucial weaknesses of testing as discussed above. As a re-
sult, even though the other weakness of testing remains (testing for one set
of inputs says nothing at all about behaviour with another set of inputs),
testing does become far more e↵ective if a system has been developed in a
functional style.
By avoiding state functional programming also avoids all of the other
state-related weaknesses discussed above, so — for example — informal
reasoning also becomes much more e↵ective.
5.2.2 Control
Most functional languages specify implicit (left-to-right) sequencing (of cal-
culationoffunctionarguments)andhencetheyfacemanyofthesameissues
mentioned above. Functional languages do derive one slight benefit when
15

---
Page 16
---

it comes to control because they encourage a more abstract use of control
using functionals (such as fold / map) rather than explicit looping.
There are also concurrent versions of many functional languages, and
the fact that state is generally avoided can give benefits in this area (for
example in a pure functional language it will always be safe to evaluate all
arguments to a function in parallel).
5.2.3 Kinds of State
In most of this paper when we refer to “state” what we really mean is
mutable state.
In languages which do not support (or discourage) mutable state it is
common to achieve somewhat similar e↵ects by means of passing extra pa-
rameters to procedures (functions). Consider a procedure which performs
some internal stateful computation and returns a result — perhaps the pro-
cedure implements a counter and returns an incremented value each time it
is called:
procedure int getNextCounter()
// ’counter’ is declared and initialized elsewhere in the code
counter := counter + 1
return counter
The way that this is typically implemented in a basic functional pro-
gramming language is to replace the stateful procedure which took no ar-
guments and returned one result with a function which takes one argument
and returns a pair of values as a result.
function (int,int) getNextCounter(int oldCounter)
let int result = oldCounter + 1
let int newCounter = oldCounter + 1
return (newCounter, result)
There is then an obligation upon the caller of the function to make
sure that the next time the getNextCounter function gets called it is sup-
pliedwiththenewCounterreturnedfromthepreviousinvocation.E↵ectively
what is happening is that the mutable state that was hidden inside the
getNextCounter procedure is replaced by an extra parameter on both the
input and output of the getNextCounter function. This extra parameter is
not mutable in any way (the entity which is referred to by oldCounter is a
di↵erent value each time the function is called).
16

---
Page 17
---

As we have discussed, the functional version of this program is refer-
entially transparent, and the imperative version is not (hence the caller of
the getNextCounter procedure has no idea what may influence the result
he gets — it could in principle be dependent upon many, many di↵erent
hidden mutable variables — but the caller of the getNextCounter function
can instantly see exactly that the result can depend only on the single value
supplied to the function).
Despite this, the fact is that we are using functional values to simulate
state. There is in principle nothing to stop functional programs from pass-
ing a single extra parameter into and out of every single function in the
entire system. If this extra parameter were a collection (compound value)
of some kind then it could be used to simulate an arbitrarily large set of
mutable variables. In e↵ect this approach recreates a single pool of global
variables — hence, even though referential transparency is maintained, ease
of reasoning is lost (we still know that each function is dependent only upon
its arguments, but one of them has become so large and contains irrelevant
values that the benefit of this knowledge as an aid to understanding is al-
most nothing). This is however an extreme example and does not detract
from the general power of the functional approach.
It is worth noting in passing that — even though it would be no substi-
tute for a guarantee of referential transparency — there is no reason why
thefunctionalstyleofprogrammingcannotbeadoptedinstatefullanguages
(i.e. imperativeaswellasimpurefunctionalones). Moregenerally,wewould
argue that — whatever the language being used — there are large benefits
to be had from avoiding hidden, implicit, mutable state.
5.2.4 State and Modularity
It is sometimes argued (e.g. [vRH04, p315]) that state is important because
it permits a particular kind of modularity. This is certainly true. Working
within a stateful framework it is possible to add state to any component
without adjusting the components which invoke it. Working within a func-
tional framework the same e↵ect can only be achieved by adjusting every
single component that invokes it to carry the additional information around
(as with the getNextCounter function above).
There is a fundamental trade o↵ between the two approaches. In the
functionalapproach(whentryingtoachievestate-likeresults)youareforced
tomakechangestoeverypartoftheprogramthatcouldbea↵ected(adding
the relevant extra parameter), in the stateful you are not.
But what this means is that in a functional program you can always tell
17

---
Page 18
---

exactly what will control the outcome of a procedure (i.e. function) simplyby
lookingatthe arguments suppliedwhere itis invoked. Ina statefulprogram
thisproperty(againaconsequenceofreferential transparency)iscompletely
destroyed, you can never tell what will control the outcome, and potentially
have to look at every single piece of code in the entire system to determine
this information.
The trade-o↵ is between complexity (with the ability to take a shortcut
when making some specific types of change) and simplicity (with huge im-
provements in both testing and reasoning). As with the discipline of (static)
typing, it is trading a one-o↵ up-front cost for continuing future gains and
safety (“one-o↵” because each piece of code is written once but is read,
reasoned about and tested on a continuing basis).
A further problem with the modularity argument is that some examples
— such as the use of procedure (function) invocation counts for debugging /
performance-tuningpurposes—seemtobebetteraddressedwithinthesup-
porting infrastructure / language, rather than within the system itself (we
prefertoadvocateaclearseparationbetweensuchadministrative/diagnostic
information and the core logic of the system).
Still, the fact remains that such arguments have been insu cient to
resultinwidespreadadoptionoffunctionalprogramming. Wemusttherefore
conclude that the main weakness of functional programming is the flip side
of its main strength — namely that problems arise when (as is often the
case) the system to be built must maintain state of some kind.
The question inevitably arises of whether we can find some way to “have
our cake and eat it”. One potential approach is the elegant system of mon-
ads used by Haskell [Wad95]. This does basically allow you to avoid the
problem described above, but it can very easily be abused to create a state-
ful, side-e↵ecting sub-language (and hence re-introduce all the problems we
are seeking to avoid) inside Haskell — albeit one that is marked by its type.
Again, despite their huge strengths, monads have as yet been insu cient to
give rise to widespread adoption of functional techniques.
5.2.5 Summary — Functional Programming
Functional programming goes a long way towards avoiding the problems
of state-derived complexity. This has very significant benefits for testing
(avoiding what is normally one of testing’s biggest weaknesses) as well as
for reasoning.
18

---
Page 19
---

5.3 Logic Programming
Together with functional programming, logic programming is considered to
be a declarative style of programming because the emphasis is on specifying
what needs to be done rather than exactly how to do it. Also as with
functional programming — and in contrast with OOP — its principles and
thewayofthinkingencourageddonot derivefromthestatefulvon-Neumann
architecture.
Pure logic programming is the approach of doing nothing more than
making statements about the problem (and desired solutions). This is done
by stating a set of axioms which describe the problem and the attributes
required of something for it to be considered a solution. The ideal of logic
programming is that there should be an infrastructure which can take the
raw axioms and use them to find or check solutions. All solutions are formal
logical consequences of the axioms supplied, and “running” the system is
equivalent to the construction of a formal proof of each solution.
The seminal “logic programming” language was Prolog. Prolog is best
seen as a pure logical core (pure Prolog) with various extra-logical5 exten-
sions. Pure Prolog is close to the ideals of logic programming, but there
are important di↵erences. Every pure Prolog program can be “read” in two
ways—eitherasapure set of logical axioms (i.e. assertionsabouttheprob-
lem domain — this is the pure logic programming reading), or operationally
— as a sequence of commands which are applied (in a particular order) to
determine whether a goal can be deduced (from the axioms). This second
reading corresponds to the actual way that pure Prolog will make use of the
axioms when it tries to prove goals. It is worth noting that a single Prolog
program can be both correct when read in the first way, and incorrect (for
example due to non-termination) when read in the second.
It is for this reason that Prolog falls short of the ideals of logic pro-
gramming. Specifically it is necessary to be concerned with the operational
interpretation of the program whilst writing the axioms.
5.3.1 State
Pure logic programming makes no use of mutable state, and for this reason
profits from the same advantages in understandability that accrue to pure
functional programming. Many languages based on the paradigm do how-
ever provide some stateful mechanisms. In the extra-logical part of Prolog
5Weareusingthetermheretocovereverything apartfromthepurecoreofProlog—
for example we include what are sometimes referred to as the meta-logical features
19

---
Page 20
---

for example there are facilities for adjusting the program itself by adding
new axioms for example. Other languages such as Oz (which has its roots
in logic programming but has been extended to become “multi-paradigm”)
providemutablestateinatraditionalway—similartothewayitisprovided
by impure functional languages.
All of these approaches to state sacrifice referential transparency and
hence potentially su↵er from the same drawbacks as imperative languages
in this regard. The one advantage that all these impure non-von-Neumann
derivedlanguagescanclaimisthat—whilststateispermitteditsuseisgen-
erally discouraged (which is in stark contrast to the stateful von-Neumann
world). Still, without purity there are no guarantees and all the same state-
related problems can sometimes occur.
5.3.2 Control
In the case of pure Prolog the language specifies both an implicit ordering
fortheprocessingofsub-goals(lefttoright),andalsoanimplicit orderingof
clauseapplication(topdown)—thesebasicallycorrespondtoanoperational
commitment to process the program in the same order as it is read textually
(in a depth first manner). This means that some particular ways of writing
downtheprogramcanleadtonon-termination, and—whencombinedwith
the fact that some extra-logical features of the language permit side-e↵ects
— leads inevitably to the standard di culty for informal reasoning caused
by control flow. (Note that these reasoning di culties do not arise in ideal
world of logic programming where there simply is no specified control — as
distinct from in pure Prolog programming where there is).
As for Prolog’s other extra-logical features, some of them further widen
the gap between the language and logic programming in its ideal form. One
example of this is the provision of “cuts” which o↵er explicit restriction of
control flow. These explicit restrictions are intertwined with the pure logic
component of the system and inevitably have an adverse a↵ect on attempts
to reason about the program (misunderstandings of the e↵ects of cuts are
recognised to be a major source of bugs in Prolog programs [SS94, p190]).
Itisworthnotingthatsomemoremodernlanguagesofthelogicprogram-
ming family o↵er more flexibility over control than the implicit depth-first
search used by Prolog. One example would be Oz which o↵ers the ability
to program specific control strategies which can then be applied to di↵erent
problemsasdesired. Thisisaveryusefulfeaturebecauseitallowssignificant
explicit control flexibility to be specified separately from the main program
(i.e. without contaminating it through the addition of control complexity).
20

---
Page 21
---

5.3.3 Summary — Logic Programming
One of the most interesting things about logic programming is that (despite
the limitations of some actual logic-based languages) it o↵ers the tantalising
promise of the ability to escape from the complexity problems caused by
control.
