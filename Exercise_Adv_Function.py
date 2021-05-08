class Solution:

    def sortby_firstletter_of_second_element(self,lst):
        sorted_activities = sorted(lst, key=lambda x: x[1], reverse=False)

        print(sorted_activities)


lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
s = Solution()
s.sortby_firstletter_of_second_element(lst)

nums = [3,4,5,2]


print(nums)