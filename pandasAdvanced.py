from functools import reduce

list_nums = [1,3,4,5,6,7]
print(list_nums)
evens = list(filter(lambda num: ( (num>5) & (num%2 == 0)),list_nums))
odds = list(filter(lambda num: num%2 != 0,list_nums))
add_by_one = list(map(lambda num: num+1,list_nums))

print("evens",evens)
print("odds",odds)
print("Add one to all",add_by_one)
sum_all = reduce(lambda a,b: a+b,add_by_one)
print(sum_all)
