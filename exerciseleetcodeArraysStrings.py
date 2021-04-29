from typing import List

class Solution:

    def moveZerosToBack(self, nums:List[int]) -> None:
        print("moveZerosToBack")
        print(nums)
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j = j+1
        else:
            for c_index in range(j,len(nums)):
                nums[c_index] = 0

        print(nums)

        # Time Complexity: O(2n) => O(n) [Linear algorithm]
        # Space Complexity: 0(1)

    def moveZerosToFront(self, nums: List[int]) -> None:
        print("moveZerosToFront")
        print(nums)
        j = len(nums)-1

        for c_index in range(len(nums)-1,-1,-1):
            if nums[c_index] != 0:
                nums[j] = nums[c_index]
                j= j-1
        else:
            for c_index in range(j+1):
                nums[c_index] = 0

        print(nums)


        # Time Complexity: O(2n) => O(n) [Linear algorithm]
        # Space Complexity: 0(1)

    def boats_to_save_people(self,persons_weight:List[int],max_weight:int):
        persons_weight.sort();
        print(persons_weight)

        left = 0;
        right = len(persons_weight)-1
        no_of_boats = 0

        while(left <= right):
            if left == right:
                no_of_boats = no_of_boats + 1
                break;
            elif persons_weight[left] + persons_weight[right] <= max_weight:
                left = left+1
            no_of_boats = no_of_boats+1
            right = right-1

        print(no_of_boats)

        # Time Complexity: O(nlog(n)) - because of Sorting Algorithm
        # Space Complexity: 0(n)

    def valid_mountain_array(self,nums:List[int]):
        j = 1
        while j < len(nums) and nums[j] > nums[j-1]:
            j += 1

        if j == 1 or j == len(nums):
            return False

        while j < len(nums) and nums[j] < nums[j-1]:
            j += 1

        return j == len(nums)
    # Time Complexity: O(N)
    # Space Complexity: O(1)


solution = Solution()
nums = [1,2,3,4,0,0,5,4,0,4,6]
persons_weight = [2,2,1,1,1,1,1,1,3]
# solution.moveZerosToBack(nums)
# solution.moveZerosToFront(nums)
# solution.boats_to_save_people(persons_weight,3)
print(solution.valid_mountain_array([0,2,3,4,5,2,1]))