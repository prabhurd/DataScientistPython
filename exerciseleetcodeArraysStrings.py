'''
Ex:1 Move Zeros elements to end of the array
'''

array_int = [1,0,3,4,4,0,0,0,5,6,7]

print(array_int)

j = 0
for num in array_int:
    if num != 0:
        array_int[j] = num
        j = j+1
else:
    for c_index in range(j,len(array_int)):
        array_int[c_index] = 0

print(array_int)