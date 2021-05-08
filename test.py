
lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]

# lambda lst:lst[1]
#
#
# lst.sort(key=lambda lst_element:lst_element[1])
# print(lst)
#
# lambda id,city:city


lst.sort(key=lambda idname,city:city)
print(lst)