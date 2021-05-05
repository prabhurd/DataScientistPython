def even_numbers(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even


def odd_numbers(numbers):
    odd = []
    for num in numbers:
        if num % 2 != 0:
            odd.append(num)
    return odd


def sum_numbers(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum


# getSumOfOddNumbers 30
def sum_even_numbers(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return sum(even)


def sum_odd_numbers(numbers):
    odd = []
    for num in numbers:
        if num % 2 != 0:
            odd.append(num)
    return sum(odd)


def map_logic_numbers(numbers):
    list_new = []
    for num in numbers:
        if num % 2 == 0:
            list_new.append(num + 1)
        else:
            list_new.append(num + 2)
    return list_new

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(even_numbers(list_numbers))
print(odd_numbers(list_numbers))
print(sum_numbers(list_numbers))
print(sum_odd_numbers(list_numbers))
print(sum_even_numbers(list_numbers))
print(map_logic_numbers(list_numbers))