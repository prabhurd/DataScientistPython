from dataclasses import dataclass

@dataclass
class Party:
    fname: str
    lname: str
    risk_score: int


def normalizeObject(obj):
    dict_new = {}
    dict_new["fname"] = obj.fname
    dict_new["lname"] = obj.lname
    dict_new["name"] = str.upper(str(obj.fname +" "+ obj.lname))
    return dict_new

parties = []
p1 = Party("prabhu","rd",5)
p2 = Party("sachin","Tendulkar",5)
p3 = Party("rahul","dravid",5)
parties.append(p1)
parties.append(p2)
parties.append(p3)


list_test = list(map(normalizeObject,parties))

for part in list_test:
    print(part)