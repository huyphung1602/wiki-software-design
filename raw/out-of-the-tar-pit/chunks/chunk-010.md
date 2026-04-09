# 10 Example of an FRP system

10 Example of an FRP system
We now examine a simple example FRP system. The system is designed
to support an estate agency (real estate) business. It will keep track of
properties which are being sold, o↵ers which are made on the properties,
53

---
Page 54
---

decisions made on the o↵ers by the owners, and commission fees earnt by
the individual agency employees from their successful sales. The example
should serve to highlight the declarative nature of the components of an
FRP system.
To keep things simple, this system operates under some restrictions:
1. Sales only — no rentals / lettings
2. Peopleonlyhaveonehome,andtheownersresideatthepropertythey
are selling
3. Rooms are perfectly rectangular
4. O↵er acceptance is binding (ie an accepted o↵er constitutes a sale)
The example will use syntax from a hypothetical FRP infrastructure
(whichsupportsnotonlytherelationalalgebrabutalsosomeofthecommon
extensions from section 8.5) — typewriter font is used for this.
10.1 User-defined Types
The example system makes use of a small number of custom types (see
section 9.3), some of which are just aliases for types provided by the infras-
tructure:
def alias address : string
def alias agent : string
def alias name : string
def alias price : double
def enum roomType : KITCHEN BATHROOM LIVING_ROOM
| |
def enum priceBand : LOW MED HIGH PREMIUM
| | |
def enum areaCode : CITY SUBURBAN RURAL
| |
def enum speedBand : VERY_FAST FAST MEDIUM SLOW
| | | |
VERY_SLOW
10.2 Essential State
The essential state (see section 9.1.1) consists of the definitions of the types
of the base relvars (the types of the attributes are shown in italics).
def relvar Property :: {address:address price:price
photo:filename agent:agent dateRegistered:date}
54

---
Page 55
---

def relvar Offer :: {address:address offerPrice:price
offerDate:date bidderName:name bidderAddress:address}
def relvar Decision :: {address:address offerDate:date
bidderName:name bidderAddress:address decisionDate:date
accepted:bool}
def relvar Room :: {address:address roomName:string
width:double breadth:double type:roomType}
def relvar Floor :: {address:address roomName:string
floor:int}
def relvar Commission :: {priceBand:priceBand
areaCode:areaCode saleSpeed:speedBand commission:double}
The example makes use of six base relations, most of which are self-
explanatory.
The Property relation stores all properties sold or for-sale. As will be
seen in section 10.3.3, properties are uniquely identified by their address.
The price is the desired sale price, the agent is the agency employee respon-
sible for selling the Property, and the dateRegistered is the date that the
Property was registred for sale with the agency.
The O↵er relation records the history of all o↵ers ever made. The ad-
dress represents the Property on which the O↵er is being made (by the
bidderName who lives at bidderAddress). The o↵erDate attribute records
the date when the o↵er was made, and the o↵erPrice records the price of-
fered. O↵ers are uniquely identified by an (address, o↵erDate, bidderName,
bidderAddress) combination.
The Decision relation records the decisions made by the owner on the
O↵ers that have been made. The O↵er in question is identified by the
(address, o↵erDate, bidderName, bidderAddress) attributes, and the date
and outcome of the decision are recorded by (decisionDate and accepted).
The Room relation records information (width, breadth, type) about the
rooms that exist at each Property. The Property is of course represented
by the address. One point worthy of note (because it’s slightly artificial) is
that an assumption is made that every Room in each Property has a unique
(within the scope of that Property) roomName. This is necessary because
many properties may have more than one room of a given type (and size).
The Floor relation records which floor each Room (roomName, address)
is on.
55

---
Page 56
---

Finally, the Commission relation stores commission fees that can be
earned by the agency employees. The commission fees are assigned on the
basis of sale prices divided into di↵erent priceBands, Property addresses
categorized into areaCodes and ratings of the saleSpeed. (The decision has
been made to represent commission rates as a base relation — rather than
as a function — so that the commission fees can be queried and easily
adjusted).
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
10.4 Accidental State and Control
Theaccidentalstateandcontrol componentofanFRPsystemconsistssolely
of a set of declarations which represent performance hints for the infrastruc-
ture (see section 9.1.3). In this example the accidental state and control is
a set of three hint declarations.
declare store PropertyInfo
This declaration is simply a hint to the infrastructure to request that
the PropertyInfo derived relation is actually stored (ie cached) rather than
continually recalculated.
62

---
Page 63
---

declare store shared Room Floor
Thishintinstructstheinfrastructuretodenormalize theRoomandFloor
relations into a single shared storage structure. (Note that because we are
able to express this as part of the accidental state and control we have not
beenforcedtocompromisetheessential partsofoursystemwhichstilltreat
Room and Floor separately).
declare store separate Property (photo)
This hint instructs the infrastructure to store the photo attribute of
the Property relation separately from its other attributes (because it is not
frequently used).
These three hints have all focused on state (PropertyInfo is accidental
state, and the other two declarations are concerned with accidental aspects
of state). Larger systems would probably also include accidental control
specifications for performance reasons.
10.5 Other
The feeders and observers for this system would be fairly simple — feeding
user input into Decisions, O↵ers etc., and directly observing and displaying
the various derived relations as output (e.g. OpenO↵ers, PropertyForWeb-
Site and CommisionDue).
Because of this it is reasonable to expect that the feeders and observers
would require no custom coding at all, but could instead be specified in a
completely declarative fashion.
One extension which might require a custom observer would be a re-
quirement to connect CommissionDue into an external payroll system.
