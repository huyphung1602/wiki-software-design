# 10.1 User-defined Types

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
