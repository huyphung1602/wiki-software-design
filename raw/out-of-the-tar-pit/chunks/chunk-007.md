# 7 Recommended General Approach

7 Recommended General Approach
Given that our main recommendations revolve around trying to avoid as
much accidental complexity as possible, we now need to look at which bits
of the complexity must be considered accidental and which essential.
We shall answer this by considering exactly what complexity could not
possibly be avoided even in the ideal world (this is basically how we define
essential). We then follow this up with a look at just how realistic this ideal
world really is before finally giving some recommendations.
7.1 Ideal World
In the ideal world we are not concerned with performance, and our language
and infrastructure provide all the general support we desire. It is against
thisbackgroundthatwearegoingtoexaminestate andcontrol. Specifically,
we are going to identify state as accidental state if we can omit it in this
ideal world, and the same applies to control.
Even in the ideal world we need to start somewhere, and it seems rea-
sonable to assume that we need to start with a set of informal requirements
from the prospective users.
Our next observation is that because we ultimately need something to
happen — i.e. we are going to need to have our system processed mechan-
ically (on a computer) — we are going to need formality. We are going to
need to derive formal requirements from the informal ones.
So, taken together, this means that even in the ideal world we have:
Informal requirements Formal requirements
!
Note that given that we’re aiming for simplicity, it is crucial that the
formalisation be done without adding any accidental aspects at all. Specifi-
cally this means that in the ideal world, formalisation must be done with no
view to execution whatsoever. The sole concern when producing the formal
requirements must be to ensure that there is no relevant6 ambiguity in the
informal requirements (i.e. that it has no omissions).
So, having produced the formalised requirements, what should the next
stepbe? Giventhatweareconsideringtheidealworld,itisnotunreasonable
6Weincludetheword“relevant”herebecauseinmanycasestheremaybemanypossible
acceptable solutions — and in such cases the requirements can be ambiguous in that
regard, however that is not considered to be a “relevant” ambiguity, i.e. it does not
correspond to an erroneous omission from the requirements.
23

---
Page 24
---

to assume that the next step is simply to execute these formal requirements
directly on our underlying general purpose infrastructure.7
Thisstateofa↵airsisabsolute simplicity—itdoesnotseemconceivable
that we can do any better than this even in an ideal world.
It is interesting to note that e↵ectively what we have just described is in
fact the very essence of declarative programming — i.e. that you need only
specify what you require, not how it must be achieved.
We now consider the implications of this “ideal” approach for the causes
of complexity discussed above.
7.1.1 State in the ideal world
Our main aim for state in the ideal world is to get rid of it — i.e. we are
hoping that most state will turn out to be accidental state.
Westartfromtheperspectiveoftheusers’informalrequirements. These
will mention data of various kinds — some of which can give rise to state
— and it is these kinds which we now classify.
Alldatawilleitherbeprovideddirectlytothesystem(input)orderived.
Additionally, derived data is either immutable (if the data is intended only
for display) or mutable (if explicit reference is made within the requirements
to the ability of users to update that data).
All data mentioned in the users’ informal requirements is of concern to
the users, and is as such essential. The fact that all such data is essential
does not however mean that it will all unavoidably correspond to essential
state. It may well be possible to avoid storing some such data, instead
dealing with it in some other essential aspect of the system (such as the
logic) — this is the case with derived data, as we shall see. In cases where
this is possible the data corresponds to accidental state.
Input Data
Data which is provided directly (input) will have to have been included
in the informal requirements and as such is deemed essential. There are
basically two cases:
There is (according to the requirements) a possibility that the system
•
may be required to refer to the data in the future.
There is no such possibility.
•
7In the presence of irrelevant ambiguities this will mean that the infrastructure must
choose one of the possibilities, or perhaps even provide all possible solutions
24

---
Page 25
---

In the first case, even in the ideal world, the system must retain the data
and as such it corresponds to essential state.
In the second case (which will most often happen when the input is
designed simply to cause some side-e↵ect) the data need not be maintained
at all.
Essential Derived Data — Immutable
Data of this kind can always be re-derived (from the input data — i.e. from
the essential state) whenever required. As a result we do not need to store
it in the ideal world (we just re-derive it when it is required) and it is clearly
accidental state.
Essential Derived Data — Mutable
As with immutable essential derived data, this can be excluded (and the
data re-derived on demand) and hence corresponds to accidental state.
Mutability of derived data makes sense only where the function (logic)
used to derive the data has an inverse (otherwise — given its mutability
— the data cannot be considered derived on an ongoing basis, and it is
e↵ectively input). An inverse often exists where the derived data represents
simplerestructuringsoftheinputdata. Inthissituationmodificationstothe
data can simply be treated identically to the corresponding modifications to
the existing essential state.
Accidental Derived Data
State which is derived but not in the users’ requirements is also accidental
state. Consider the following imperative pseudo-code:
procedure int doCalculation(int y)
// ’subsidaryCalcCache’ is declared and initialized
// elsewhere in the code
if (subsidaryCalcCache.contains(y) == false) {
subsidaryCalcCache.y := slowSubsidaryCalculation(y)
}
return 3 * (4 + subsidaryCalcCache.y)
The above use of state in the doCalculation procedure seems to be
unnecessary (in the ideal world), and hence of the accidental variety. We
25

---
Page 26
---

Data Essentiality Data Type Data Mutability Classification
Essential Input - Essential State
Essential Derived Immutable Accidental State
Essential Derived Mutable Accidental State
Accidental Derived - Accidental State
Table 1: Data and State
cannot actually be sure without knowing whether and how the subsidary-
CalcCache is used elsewhere in the program, but for this example we shall
assume that there are no other uses aside from initialization. The above
procedure is thus equivalent to:
procedure int doCalculation(int y)
return 3 * (4 + slowSubsidaryCalculation(y))
It is almost certain that this use of state would not have been part of
the users’ informal requirements. It is also derived. Hence, it is quite clear
that we can eliminate it completely from our ideal world, and that hence it
is accidental.
Summary — State in the ideal world
For our ideal approach to state, we largely follow the example of functional
programming which shows how mutable state can be avoided. We need to
remember though that:
1. even in the ideal world we are going to have some essential state —
as we have just established
2. pure functional programs can e↵ectively simulate accidental state in
the same way that they can simulate essential state (using techniques
such as the one discussed above in section 5.2.3) — we obviously want
to avoid this in the ideal world.
The data type classifications are summarized in Table 1. Wherever the
table shows data as corresponding to accidental state it means that it can
be excluded from the ideal world (by re-deriving the data as required).
The obvious implication of the above is that there are large amounts of
accidental state in typical systems. In fact, it is our belief that the vast
majority of state (as encountered in typical contemporary systems) simply
26
[Image: page-026-fig-01.png]


---
Page 27
---

isn’t needed (in this ideal world). Because of this, and the huge complexity
whichstatecancause, theidealworldremovesall non-essentialstate. There
is no other state at all. No caches, no stores of derived calculations of any
kind. One e↵ect of this is that all the state in the system is visible to the
user of (or person testing) the system (because inputs can reasonably be
expected to be visible in ways which internal cached state normally is not).
7.1.2 Control in the ideal world
Whereas we have seen that some state is essential, control generally can be
completely omitted from the ideal world and as such is considered entirely
accidental. It typically won’t be mentioned in the informal requirements
and hence should not appear in the formal requirements (because these are
derived with no view to execution).
What do we mean by this? Clearly if the program is ever to run, some
control will be needed somewhere because things will have to happen in
some order — but this should no more be our concern than the fact that the
chancesaresomeelectricitywillbeneededsomewhere. Theimportantthing
is that we (as developers of the system) should not have to worry about the
control flow in the system. Specifically the results of the system should be
independent of the actual control mechanism which is finally used.
These are precisely the lessons which logic programming teaches us, and
because of this we would like to take the lead for our ideal approach to
control from logic programming which shows that control can be separated
completely.
It is worth noting that because typically the informal requirements will
not mention concurrency, that too is normally of an accidental nature. In
an ideal world we can assume that finite (stateless) computations take zero
time8 andassuchitisimmaterialtoauserwhethertheyhappeninsequence
or in parallel.
7.1.3 Summary
In the ideal world we have been able to avoid large amounts of complexity
— both state and control. As a result, it is clear that a lot of complexity
is accidental. This gives us hope that it may be possible to significantly
reduce the complexity of real large systems. The question is — how close is
it possible to get to the ideal world in the real one?
8this assumption is generally known as the “synchrony hypothesis”
27

---
Page 28
---

7.2 Theoretical and Practical Limitations
The real world is not of course ideal. In this section we examine a few of
the assumptions made in the section 7.1 and see where they break down.
As already noted, our vision of an ideal world is similar in many ways to
the vision of declarative programming that lies behind functional and logic
programming.
Unfortunately we have seen that functional and logic programming ul-
timately had to confront both state and control. We should note that the
reasons for having to confront each are slightly di↵erent. State is required
simplybecausemostsystemsdohavesomestateaspartoftheirtrueessence.
Control generally is accidental (the users normally are not concerned about
it at all) but the ability to restrict and influence it is often required from a
practical point of view. Additionally practical (e.g. e ciency) concerns will
often dictate the use of some accidental state.
These observations give some indication of where we can expect to en-
counter di culties.
7.2.1 Formal Specification Languages
First of all, we want to consider two problems (one of a theoretical kind,
the other practical) that arise in connection with the ideal-world formal
requirements.
In that section we discussed the need for formal requirements derived
directly from the informal requirements. We observed that in the ideal
world we would like to be able to execute the formal requirements without
first having to translate them into some other language.
The phrase “formal requirements” is basically synonymous with “for-
mal specification”, so what e↵ectively we’re saying would be ideal are exe-
cutable specifications. Indeed both the declarative programming paradigms
discussedabove(functionalprogrammingandlogicprogramming)havebeen
proposed as approaches for executable specifications.
Before we consider the problems with executing them, we want to com-
mentthatthewayinwhich theidealworldformalspecificationswerederived
— directly from the users’ informal requirements — was critical. Formal
specifications can be derived in various other ways (some of which risk the
introductionofaccidentalcomplexity), andcanbeofvariousdi↵erentkinds.
Traditionally formal specification has been categorized into two main
camps:
Property-based approaches focus (in a declarative manner) on what is
28

---
Page 29
---

required rather than how the requirements should be achieved. These
approaches include the algebraic (equational axiomatic semantics) ap-
proaches such as Larch and OBJ.
Model-based (or State-based) approaches construct a potential model
for the system (often a stateful model) and specify how that model
mustbehave. Theseapproaches(whichincludeZandVDM)canhence
be used to specify how a stateful, imperative language solution must
behave to satisfy the requirements. (We discussed the weaknesses of
stateful imperative languages in section 5).
The first problem that we want to discuss in this section is the more
theoretical one. Arguments (which focus more on the model-based ap-
proaches) have been put forward against the concept of executable spec-
ifications [HJ89]. The main objection is that requiring a specification lan-
guage to be executable can directly restrict its expressiveness (for example
when specifying requirements for a variable x it may be desirable to assert
something like y f(y,x) which clearly has no direct operational interpre-
¬9 |
tation).
In response to this objection, we would say firstly that in our experience
a requirement for this kind of expressivity does not seem to be common in
many problem domains. Secondly it would seem sensible that where such
specifications do occur they should be maintained in their natural form
but supplemented with a separate operational component. Indeed in this
situation it would not seem too unreasonable to consider the required oper-
ational component to be accidental in nature (of course the reality is that in
cases like this the boundary between what is accidental and essential, what
is reasonable to hope for in an “ideal” world, becomes less clear). Some
specification languages address this issue by having an executable subset.
Finally, it is the property-based approaches that seem to have the great-
est similarity to what we have in mind when we talk about executable spec-
ifications in the ideal world. It certainly is possible to execute algebraic
specifications — deriving an operational semantics by choosing a direction
for each of the equational axioms.9
In summary, the first problem is that consideration of specification lan-
guages highlights the (theoretically) fuzzy boundary between what is essen-
tial and what is accidental — specifically it challenges the validity of our
definition of essential (which we identified closely with requirements from
the users) by observing that it is possible to specify things which are not
9Care must be taken that the resulting reduction rules are confluent and terminating.
29

---
Page 30
---

directly executable. For the reasons given above (and in section 6) we think
that — from the practical point of view — our definition is still viable,
import and justified.
The second problem is of a more practical nature — namely that even
when specifications are directly executable, this can be impractical for e -
ciency reasons. Our response to this is that whilst it is undoubtedly true,
we believe that it is very important (for understanding and hence for avoid-
ing complexity) not to lose the distinction we have defined between what is
accidental and essential. As a result, this means that we will require some
accidental components as we shall see in section 7.2.3.
7.2.2 Ease of Expression
Thereisonefinalpracticalproblemthatwewanttoconsider—eventhough
we believe it is fairly rare in most application domains. In section 7.1.1 we
argued that immutable, derived data would correspond to accidental state
and could be omitted (because the logic of the system could always be used
to derive the data on-demand).
Whilstthisistrue,thereareoccasionallysituationswheretheidealworld
approach (of having no accidental state, and using on-demand derivation)
does not give rise to the most natural modelling of the problem.
Onepossiblesituationofthiskindisforderiveddatawhichisdependent
upon both a whole series of user inputs over time, and its own previous
values. In such cases it can be advantageous10 to maintain the accidental
state even in the ideal world.
An example of this would be the derived data representing the position
state of a computer-controlled opponent in an interactive game — it is at all
timesderivable byafunctionofbothallpriorusermovementsandtheinitial
starting positions,11 but this is not the way it is most naturally expressed.
7.2.3 Required Accidental Complexity
We have seen two possible reasons why in practice — even with optimal
language and infrastructure — we may require complexity which strictly is
accidental. These reasons are:
Performance making use of accidental state and control can be required
for e ciency — as we saw in the second problem of section 7.2.1.
10because it can make the logic easier to express — as we shall see in section 7.3.2
11We are implicitly considering time as an additional input.
30

---
Page 31
---

Ease of Expression making use of accidental state can be the most nat-
ural way to express logic in some cases — as we saw in section 7.2.2.
Of the two, we believe that performance will be the most common.
It is of course vital to be aware that as soon as we re-introduce this acci-
dental complexity, we are again becoming exposed to the dangers discussed
in sections 4.1 and 4.2. Specifically we can see that if we add in accidental
state which has to be managed explicitly by the logic of the system, then we
become at risk of the possibility of the system entering an inconsistent state
(or “bad state”) due to errors in that explicit logic. This is a very serious
concern, and is one that we address in our recommendations below.
7.3 Recommendations
Webelievethat—despitetheexistenceofrequiredaccidentalcomplexity—
it is possible to retain most of the simplicity of the ideal world (section 7.1)
in the real one. We now look at how this might be achievable.
Our recommendations for dealing with complexity (as exemplified by
both state and control) can be summed up as:
Avoid
•
Separate
•
Specifically the overriding aim must be to avoid state and control where
they are not absolutely and truly essential.
The recommendation of avoidance is however tempered by the acknowl-
edgement that there will sometimes be complexity that either is truly essen-
tial (section 7.1.1) or, whilst not truly essential, is useful from a practical
point of view (section 7.2.3). Such complexity must be separated out from
the rest of the system — and this gives us our second recommendation.
There is nothing particularly profound in these recommendations, but
they are worth stating because they are emphatically not the way most
software is developed today. It is the fact that current established practice
does not use these as central overriding principles for software development
that leads directly to the complexity that we see everywhere, and as already
argued, it is that complexity which leads to the software crisis12.
In addition to not being profound, the principles behind these recom-
mendations are not really new. In fact, in a classic 1979 paper Kowalski
12There is some limited similarity between our goal of “Separate” and the goal of
separation of concerns as promoted by proponents of Aspect Oriented Programming —
but as we shall see in section 7.3.2, exactly what is meant by separation is critical.
31

---
Page 32
---

(co-inventor of Prolog) argued in exactly this direction [Kow79]. The title
of his paper was the equation:
“Algorithm = Logic+Control”
...and this separation that he advocated is close to the heart of what
we’re recommending.
7.3.1 Required Accidental Complexity
In section 7.2.3 we noted two possible reasons for requiring accidental com-
plexity (even in the presence of optimal language and infrastructure). We
now consider the most appropriate way of handling each.
Performance
We have seen that there are many serious risks which arise from accidental
complexity — particularly when introduced in an undisciplined manner. To
mitigate these risks we take two defensive measures.
The first is with regard to the risks of explicit management of accidental
state (which we have argued is actually the majority of state). The rec-
ommendation here is that we completely avoid explicit management of the
accidental state — instead we should restrict ourselves to simply declaring
what accidental state should be used, and leave it to a completely separate
infrastructure(onwhichoursystemwilleventuallyrun)tomaintain. Thisis
reasonable because the infrastructure can make use of the (separate) system
logic which specifies how accidental data must be derived.
By doing this we eliminate any risk of state inconsistency (bugs in the
infrastructure aside of course). Indeed, as we shall see (in section 7.3.2),
from the point of view of the logic of the system, we can e↵ectively forget
thattheaccidentalstate evenexists. Morespecificexamplesofthisapproach
are given in the second half of this paper.
The other defensive action we take is “Separate”. We examine separa-
tion after first looking at the other possible reason for requiring accidental
complexity.
Ease of Expression
This problem (see section 7.2.2) fundamentally arises when derived (i.e.
accidental) state o↵ers the most natural way to express parts of the logic of
the system.
32

---
Page 33
---

Complexity Type Recommendation
Essential Logic Separate
Essential Complexity State Separate
Accidental Useful Complexity State / Control Separate
Accidental Useless Complexity State / Control Avoid
Table 2: Types of complexity within a system
The di culty then arises that this requirement (to use the accidental
state in a fairly direct manner inside the system logic) clashes with the goal
of separation that we have just discussed. This very separation is critical
when it comes to avoiding complexity, so we do not want to sacrifice it for
this (probably fairly rare) situation.
Instead what we recommend is that, in cases where it really is the only
natural thing to do, we should pretend that the accidental state is really
essential state for the purposes of the separation discussed below. One
straightforward way to do this is to make use of an external component
which observes the derived data in question and creates the illusion of the
user typing that same (derived, accidental) data back in as input data (we
touch on this issue again in section 9.1.4).
7.3.2 Separation and the relationship between the components
In the above we deliberately glossed over exactly what we meant by our sec-
ond recommendation: “Separate”. This is because it actually encompasses
two things.
The first thing that we’re doing is to advocate separating out all com-
plexity of any kind from the pure logic of the system (which — having
nothing to do with either state or control — we’re not really considering
part of the complexity). This could be referred to as the logic / state split
(although of course state is just one aspect of complexity — albeit the main
one).
The second is that we’re further dividing the complexity which we do
retainintoaccidentalandessential.Thiscouldbereferredtoastheaccidental
/ essential split. These two splits can more clearly be seen by considering
the Table 2. (N.B. We do not consider there to be any essential control).
The essential bits correspond to the requirements in the ideal world of
section 7.1 — i.e. we are recommending that the formal requirements adopt
the logic / state split.
The top three rows of the table correspond to components which we
33
[Image: page-033-fig-01.png]


---
Page 34
---

expect to exist in most practical systems (some systems may not actually
require any essential state, but we include it here for generality). i.e. These
are the three things which will need to be specified (in terms of a given
underlying language and infrastructure) by the development team.
“Separate” is basically advocating clean distinction between all three of
these components. It is additionally advocating a split between the state
and control components of the “Useful” Accidental Complexity — but this
distinction is less important than the others.
One implication of this overall structure is that the system (essential +
accidental but useful) should still function completely correctly if the “acci-
dental but useful” bits are removed (leaving only the two essential compo-
nents) — albeit possibly unacceptably slowly. As Kowalski (who — writing
in a Prolog-context — was not really considering any essential state) says:
“The logic component determines the meaning ...whereas the
control component only a↵ects its e ciency”.
A consequence of separation is that the separately specified components
will each be of a very di↵erent nature, and as a result it may be ideal to
use di↵erent languages for each. These languages would each be oriented
(i.e. restricted) to their specific goal — there is no sense in having control
specification primitives in a language for specifying state. This notion of
restricting the power of the individual languages is an important one —
the weaker the language, the more simple it is to reason about. This has
something in common with the ideas behind “Domain Specific Languages”
— one exception being that the domains in question are of a fairly abstract
nature and combine to form a general-purpose platform.
The vital importance of separation comes simply from the fact that it is
separation that allows us to “restrict the power” of each of the components
independently. The restricted power of the respective languages with which
each component is expressed facilitates reasoning about them individually.
Theveryfactthatthethreeareseparatedfromeachotherfacilitatesreason-
ing about them as a whole (e.g. you do not have to think about accidental
state at all when you are working on the essential logic of your system13).
Figure 1 shows the same three expected components of a system in a
di↵erent way (compare with Table 2). Each box in the diagram corresponds
to some aspect of the system which will need to be specified by the devel-
opment team. Specifically, it will be necessary to specify what the essential
13indeed it should be perfectly possible for di↵erent users of the same essential system
to employ di↵erent accidental components — each designed for their particular needs
34

---
Page 35
---

Essential
-
Logic
Accidental
State and
Control ?
- Essential
State
Language and Infrastructure
Figure 1: Recommended Architecture (arrows show static references)
statecanbe, whatmustalwaysbelogicallytrue, andfinallywhataccidental
use can be made of state and control (typically for performance reasons).
The di↵ering nature of what is specified by each of the components
leads naturally to certain relationships between them, to restrictions on the
ways in which they can or cannot refer to each other. These restrictions
are absolute, and because of this provide a huge aid to understanding the
di↵erent components of the system independently.
Essential State This can be seen as the foundation of the system. The
specification of the required state is completely self-contained — it
can make no reference to either of the other parts which must be
specified. One implication of this is that changes to the essential state
specificationitselfmayrequirechangesinboththeotherspecifications,
but changes in either of the other specifications may never require
changes to the specification of essential state.
Essential Logic This is in some ways the “heart” of the system — it ex-
presses what is sometimes termed the “business” logic. This logic
expresses — in terms of the state — what must be true. It does not
say anything about how, when, or why the state might change dy-
namically — indeed it wouldn’t make sense for the logic to be able to
change the state in any way.
Changes to the essential state specification may require changes to
the logic specification, and changes to the logic specification may re-
quirechangestothespecificationforaccidentalstateandcontrol. The
logic specification will make no reference to any part of the accidental
35
[Image: page-035-fig-01.png]


---
Page 36
---

specification. Changes in the accidental specification can hence never
require any change to the essential logic.
Accidental State and Control This (by virtue of its accidental nature)
is conceptually the least important part of the system. Changes to
it can never a↵ect the other specifications (because neither of them
make any reference to any part of it), but changes to either of the
others may require changes here.
Together the goals of avoid and separate give us reason to hope that we
may well be able to retain much of the simplicity of the ideal world in the
real one.
7.4 Summary
Thisfirstpartofthepaperhasdonetwomainthings. Ithasgivenarguments
for the overriding danger of complexity, and it has given some hope that
much of the complexity may be avoided or controlled.
The key di↵erence between what we are advocating and existing ap-
proaches (as embodied by the various styles of programming language) is a
high level separation into three components — each specified in a di↵erent
language14. It is this separation which allows us to restrict the power of
each individual component, and it is this use of restricted languages which
is vital in making the overall system easier to comprehend (as we argued in
section 4.4 — power corrupts).
Doing this separation when building a system may not be easy, but we
believe that for any large system it will be significantly less di cult than
dealing with the complexity that arises otherwise.
It is hard to overstate the dangers of complexity. If it is not controlled it
spreads. The only way to escape this risk is to place the goals of avoid and
separate at the top of the design objectives for a system. It is not su cient
simply to pay heed to these two objectives — it is crucial that they be the
overriding consideration. This is because complexity breeds complexity and
one or two early “compromises” can spell complexity disaster in the long
run.
It is worth noting in particular the risks of “designing for performance”.
The dangers of “premature optimisation” are as real as ever — there can
be no comparison between the di culty of improving the performance of a
14or di↵erent subsets of the same language, provided it is possible to forcibly restrict
each component to the relevant subset.
36

---
Page 37
---

slow system designed for simplicity and that of removing complexity from a
complex system which was designed to be fast (and quite possibly isn’t even
that because of myriad ine ciencies hiding within its complexity).
In the second half of this paper we shall consider a possible approach
based on these recommendations.
