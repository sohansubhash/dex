Locations:
- [Location ID, Name, Description, Settlement?]
- [Int, String, String, Boolean]

Building:
- [Building ID, Name, Description]
- [Int, String, String]

Trainers:
- [Trainer ID, Name, Class]
- [Int, String, String]

Items:
- [Item ID, Name, Description, Usable in Battle?, Purchaseable?, Usable on Pokemon]
- [Int, String, String, Boolean, Boolean, Boolean]

Moves:
- [Move ID, Name, Description, Damaging?, Accuracy, Damage]
- [Int, String, String, Boolean, Float, Int]

Pokemon:
- [name, dex_id, Type1, Type2, Stage, Experience Rate, HP, Attack, Special, Defense, Speed, Height, Weight]
- [String, Int, Int, Int, Int, Float, Int, Int, Int, Int, Int, Float, Float]


---


Location to Catchable Pokemon:
- [LBID, Pokemon ID, Level min, Level Max, Catch Method]
- [Int, Int, Int, Int, Int, String]

Location to Item Table:
- [LBID, Item ID]
- [Int, Int]

Location Buildings to Trainer Table:
- [LBID, Trainer ID]
- [Int, Int]

LBID to LocationID, BuildingID:
- [LBID, Locations ID, Building ID]
- [Int, Int, Int]

Trainers to Items:
- [Trainer ID, Item ID, Quantity]
- [Int, Int, Int]

Trainers to Pokemon:
- [Trainer ID, Pokemon ID, Level]
- [Int, Int, Int]

Move,Pokemon ID:
- [MID, Move ID, Pokemon ID, Learn Method (String), Level (int), Item ID, LBID]
- [Int, Int, Int, String, Int, Int, Int]

---
(Learn Methods: Levelup, Item ID, LBID)