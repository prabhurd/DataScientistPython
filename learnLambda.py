from functools import reduce
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda num: num % 2 == 0, list_numbers))
odd_numbers = list(filter(lambda num: num % 2 != 0, list_numbers))
logic_map_numbers = list(map(lambda num: num + 1 if num % 2 == 0 else num + 2, list_numbers))
sum_numbers = reduce(lambda a, b: a + b, list_numbers)
sum_even_numbers = reduce(lambda a, b: a + b, list(filter(lambda num: num % 2 == 0, list_numbers)))
sum_odd_numbers = reduce(lambda a, b: a + b, list(filter(lambda num: num % 2 != 0, list_numbers)))
factorial_number = reduce(lambda a,b: a*b,range(1,5+1))
factorial_number_list = max(list(map(lambda x: reduce(lambda a,b: a*b,range(1,x+1)),list_numbers)))


def find_max(nums):
    max_num = 0

    max_num = [num for num in nums if num > max_num]

    return max_num


print(find_max([1,3,4,2,5,6,2,11,4,5,6]))