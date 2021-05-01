# Python Lambda

def callByValue(a):
    a= "KOVILAMBAKKAM"
    return a



def callByObject(crickters):
    new_crickters = crickters
    new_crickters.append("Dravid")
    return list;

address = "CIT NAGAR"
callByValue(address)
print(address)


def callByReference(list_cricketer):
    cricket = []
    cricket.append("DRAVID")
    list_cricketer.append("DRAVID")
    return cricket

list_cricketer = ["Ganguly","Sachin"]
callByReference(list_cricketer)
print(list_cricketer)



