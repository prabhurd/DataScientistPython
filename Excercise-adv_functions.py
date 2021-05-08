from functools import reduce

class Solution:

    def sortlist_byIndexElement(self, lst, index):
        lst.sort(key=lambda element: element[index])
        return lst

    def sortlist_byLastLetter(self, lst, index):
        lst.sort(key=lambda element: element[index][-1])
        return lst

    def mergelist_byZip(self, lst):
        create_index = [index for index in range(1, len(lst) + 1)]
        zip_list = list(zip(create_index, lst))
        return zip_list



solution = Solution()
lst = [(19542209, "New York"), (4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"),
       (1805832, "West Virginia"), (39865590, "California")]
lst1 = ["Energy", "Agriculture", "Industry", "Technology", "Finance", "Forestry", "Transport"]
lst_country=["Antartica", "America", "Armania", "Australia", "Albania", "Afganistan","Alaska"]

'''Exercise 1: Write a function to sort the list based on the first letter of the second element'''
solution.sortlist_byIndexElement(lst, 1)

'''Exercise 2: Write a function to sort the list based on the last letter of the second element'''
solution.sortlist_byLastLetter(lst, 1)

'''## Exercise 3: Create a range from 1 to 8 merge the given list and together to create a new list of tuples.'''
solution.mergelist_byZip(lst1)

'''Exercise 4: Write a function and create a list consisted of the number of occurence of letter: a (all a's).'''

count_lst1 = []

for country_name in lst_country:
    count_lst1.append(country_name.lower().count('a'))

print(list(zip(lst_country,count_lst1)))


'''Exercise 5: Write a function filter all the vowels in a given string using filter.'''

str1="Inceptz is one of the best institutes to read data science in chennai"

print(list(filter(lambda x: x.lower() in ['a','e','i','o','u'],str1)))

'''Exercise 6: Write a function to create a list as the square of elements from the given list if the square is greater than 60'''

lst1_num=[5, 6, 7 , 8, 9, 10, 12, 14]

print(list(filter(lambda x: x>60,map(lambda x:x*x,lst1_num))))


'''Exercise 7: take the words given below as list and write a function and use reduce to make it a sentence'''

str_sentence = '''
Inceptz

provides

the

best

inclass

trainings

and

is

the

best
'''

str_words_list = reduce(lambda a,b: a+" "+b,filter(lambda word: word.strip() != '',str_sentence.strip().split("\n")))
print(str_words_list)