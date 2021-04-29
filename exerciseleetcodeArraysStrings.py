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

solution = Solution()
nums = [1,2,3,4,0,0,5,4,0,4,6]
solution.moveZerosToBack(nums)
solution.moveZerosToFront(nums)