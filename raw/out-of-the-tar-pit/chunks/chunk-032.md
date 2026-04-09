# 10.3 Essential Logic

10.3 Essential Logic
This is the heart of the system (see section 9.1.2) and corresponds to the
“business logic”.
10.3.1 Functions
We do not give the actual function definitions here, we just describe their
operation informally. In reality we would supply the function definitions in
terms of some language provided by the infrastructure.
priceBandForPrice Converts a price into a priceBand (which will be used
in the commission calculations)
areaCodeForAddress Converts an address into an areaCode
datesToSpeedBand Converts a pair of dates into a speedBand (reflecting
the speed of sale after taking into account the time of year)
10.3.2 Derived Relations
Therearethirteenderivedrelationsinthesystem. Thesecanbeveryloosely
classified as internal or external according to whether their main purpose is
simplytofacilitatethedefinitionofotherderivedrelations(andconstraints)
or to provide information to the users. We consider the definition and pur-
pose of each in turn.
As an aid to understanding, the types of the derived relations are shown
in comments (delimited by /* and */). In reality these types would be de-
rived (or checked) by an infrastructure-provided type inference mechanism.
Internal
The ten internal derived relations exist mainly to help with the later defi-
nition of the three external ones.
56

---
Page 57
---

/* RoomInfo :: {address:address roomName:string width:double
breadth:double type:roomType roomSize:double} */
RoomInfo = extend(Room, (roomSize = width*breadth))
The RoomInfo derived relation simply extends the Room base relation
with an extra attribute roomSize which gives the area of each room.
/* Acceptance :: {address:address offerDate:date bidderName:name
bidderAddress:address decisionDate:date} */
Acceptance = project_away(restrict(Decision | accepted == true),
accepted)
The Acceptance derived relation simply selects the positive entries from
the Decision base relation, and then strips away the accepted attribute (the
project_away operation is the dual of the project operation — it removes
the listed attributes rather than keeping them).
/* Rejection :: {address:address offerDate:date bidderName:name
bidderAddress:address decisionDate:date} */
Rejection = project_away(restrict(Decision | accepted == false),
accepted)
The Rejection derived relation simply selects the negative decisions and
removes the accepted attribute.
/* PropertyInfo :: {address:address price:price photo:filename
agent:agent dateRegistered:date
priceBand:priceBand areaCode:areaCode
numberOfRooms:int squareFeet:double} */
PropertyInfo =
extend(Property,
(priceBand = priceBandForPrice(price)),
(areaCode = areaCodeForAddress(address)),
(numberOfRooms = count(restrict(RoomInfo |
address == address))),
(squareFeet = sum(roomSize, restrict(RoomInfo |
address == address))))
The PropertyInfo derived relation extends the Property base relation
with four new attributes. The first — called priceBand — indicates which
of the estate agency’s price bands the property is in. The price band of the
57

---
Page 58
---

final sale price will a↵ect the commission derived by the agent for selling the
property. The areaCode attribute indicates the area code, which also a↵ects
the commission an agent may earn. The numberOfRooms is calculated by
counting the number of rooms (actually the number of entries in the Room-
Info derived relation at the corresponding address), and the squareFeet is
computed by summing up the relevant roomSizes.
/* CurrentOffer :: {address:address offerPrice:price
offerDate:date bidderName:name
bidderAddress:address} */
CurrentOffer =
summarize(Offer,
project(Offer, address bidderName bidderAddress),
quota(offerDate,1))
ThepurposeoftheCurrentO↵erderivedrelationistofilteroutoldo↵ers
which have been superceded by newer ones (e.g. if the bidder has submitted
a revised — higher or lower — o↵er, then we are no longer interested in
older o↵ers they may have made on the same property).
ThedefinitionsummarizestheO↵erbaserelation,takingthemostrecent
(ie the single greatest o↵erDate) o↵er made by each bidder on a property
(ie per unique address, bidderName, bidderAddress combination). Because
both bidderName and bidderAddress are included, the system supports the
(admittedly unusual) possibility of di↵erent people living in the same place
(bidderAddress) submitting di↵erent o↵ers on the same property (address).
/* RawSales :: {address:address offerPrice:price
decisionDate:date agent:agent
dateRegistered:date} */
RawSales =
project_away(join(Acceptance,
join(CurrentOffer,
project(Property, address agent
dateRegistered))),
offerDate bidderName bidderAddress)
For the purposes of this example, sales are seen as corresponding di-
rectly to accepted o↵ers. As a result the definition of the RawSales relation
is in terms of the Acceptance relation. These accepted o↵ers are augmented
(joined) with the CurrentO↵er information (which includes the agreed of-
ferPrice) and with information (agent, dateRegistered) from the Property
relation.
58

---
Page 59
---

/* SoldProperty :: {address:address} */
SoldProperty = project(RawSales, address)
The SoldProperty relation simply contains the address of all Properties
on which a sale has been agreed (ie the properties in the RawSales relation).
/* UnsoldProperty :: {address:address} */
UnsoldProperty = minus(project(Property, address), SoldProperty)
The UnsoldProperty is obviously just the Property which is not Sold-
Property (i.e. all Property addresses minus the SoldProperty addresses).
/* SalesInfo :: {address:address agent:agent areaCode:areaCode
saleSpeed:speedBand priceBand:priceBand} */
SalesInfo =
project(extend(RawSales,
(areaCode = areaCodeForAddress(address)),
(saleSpeed = datesToSpeedBand(dateRegistered,
decisionDate)),
(priceBand = priceBandForPrice(offerPrice))),
address agent areaCode saleSpeed priceBand)
The SalesInfo relation is based on the RawSales relation, but extends
it with areaCode, saleSpeed and priceBand information by calling the three
relevant functions.
/* SalesCommissions :: {address:address agent:agent
commission:double} */
SalesCommissions =
project(join(SalesInfo, Commission),
address agent commission)
TheSalesCommissionswhichareduetotheagentsarederivedsimplyby
joiningtogethertheSalesInfowiththeCommissionbaserelation. Thisgives
the amount of commission due to each agent on each Property (represented
by address).
External
Having now defined all the internal derived relations, we are now in a posi-
tion to define the external derived relations — these are the ones which will
be of most direct interest to the users of the system.
59

---
Page 60
---

/* OpenOffers :: {address:address offerPrice:price
offerDate:date bidderName:name
bidderAddress:address} */
OpenOffers =
join(CurrentOffer,
minus(project_away(CurrentOffer, offerPrice),
project_away(Decision, accepted decisionDate)))
The OpenO↵ers relation gives details of the CurrentO↵ers on which the
owner has not yet made a Decision. This is calculated by joining the Cur-
rentO↵er information (which includes o↵erPrice) with those CurrentO↵ers
(excluding the price information) that do not have corresponding Decisions.
project_away is used here because minus requires its arguments to be of
the same type.
/* PropertyForWebSite :: {address:address price:price
photo:filename numberOfRooms:int
squareFeet:double} */
PropertyForWebSite = project( join(UnsoldProperty, PropertyInfo),
address price photo
numberOfRooms squareFeet )
ThebusinesswantstodisplaytheinformationfromPropertyInfoontheir
external website. However, they only want to show unsold property (this
is achieved simply by a join), and they only want to show a subset of the
attributes (this is achieved with a project).
/* CommissionDue :: {agent:agent totalCommission:double} */
CommissionDue =
project(summarize(SalesCommissions,
project(SalesCommissions, agent),
totalCommission = sum(commission)),
agent totalCommission)
Finally, the total commission due to each agent is calculated by simply
summing up the commission attribute of the SalesCommissions relation on
a per agent basis to give the totalCommission attribute.
10.3.3 Integrity
Integrity constraints are given in the form of relational algebra or relational
calculusexpressions. Asalreadynoted, ourhypotheticalFRPinfrastructure
60

---
Page 61
---

provides common relational algebra extensions (see section 8.5). It also
provides special syntax for candidate and foreign key constraints. (This
syntax is e↵ectively just a shorthand for the underlying algebra or calculus
expression).
We consider the standard (key) constraints first:
candidate key Property = (address)
candidate key Offer = (address, offerDate,
bidderName, bidderAddress)
candidate key Decision = (address, offerDate,
bidderName, bidderAddress)
candidate key Room = (address, roomName)
candidate key Floor = (address, roomName)
candidate key Commision = (priceBand, areaCode, saleSpeed)
foreign key Offer (address) in Property
foreign key Decision (address, offerDate,
bidderName, bidderAddress) in Offer
foreign key Room (address) in Property
foreign key Floor (address) in Property
Therearealsosomeslightlymoreinteresting,domain-specificconstraints.
The first insists that all properties must have at least one room:
count(restrict(PropertyInfo | numberOfRooms < 1)) == 0
The next ensures that people cannot submit bids on their own property
(owners are assumed to be residing at the property they are selling):
count(restrict(Offer | bidderAddress == address)) == 0
This constraint prohibits the submission of any O↵ers on a property
(address) after a sale has happened (i.e. after an Acceptance has occurred
for the address):
count(restrict(join(Offer,
project(Acceptance, address decisionDate))
| offerDate > decisionDate)) == 0
Thenextconstraintensuresthattherearenevermorethan50properties
advertised on the website in the PREMIUM price band:
61

---
Page 62
---

count(restrict(extend(PropertyForWebSite,
(priceBand = priceBandForPrice(price)))
| priceBand == PREMIUM)) < 50
This is an interesting constraint because it depends (directly as it hap-
pens) on a user-defined function (priceBandForPrice). One implication of
this is that changes to function definitions (as well as changes to essential
state) could — if unchecked — cause the system to violate its constraints.
No FRP infrastructure can allow this.
Fortunately there are two straightforward approaches to solving this.
The first is that the infrastructure could treat function definitions as data
(essential state) and apply the same kind of modification checks. The alter-
native is that it could refuse to run a system with a new function version
which causes existing data to be considered invalid. In this latter case man-
ual state changes would be required to restore integrity and to allow the
system became operational again.
Finally, no single bidder can submit more than 10 o↵ers (over time) on
a single Property. This constraint works by first computing the number of
o↵ers made by each bidder (bidderName, bidderAddress) on each Property
(address), and ensuring that this is never more than 10:
count(restrict(summarize(Offer,
project(Offer, address bidderName
bidderAddress),
numberOfOffers = count())
| numberOfOffers > 10)) == 0
Oncethesystemisdeployed,theFRPinfrastructurewillrejectanystate
modificationattemptswhichwouldviolateanyoftheseintegrityconstraints.
