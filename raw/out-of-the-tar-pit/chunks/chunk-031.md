# 10.2 Essential State

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
