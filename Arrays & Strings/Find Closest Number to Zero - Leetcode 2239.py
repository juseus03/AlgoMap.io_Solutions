from typing import List
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        indx = 0
        minimum = abs(nums[0])
        for i, n in enumerate(nums):

            if minimum >  abs(n):
                minimum = abs(n)
                indx = i
            
            if minimum == abs(n):
                indx = i if n > nums[indx] else indx
            
        return nums[indx] 


# Test cases
sol = Solution()

nums = [-4,-2,1,4,8] # 1
sol.findClosestNumber(nums)
assert sol.findClosestNumber(nums) == 1

nums = [2,-1,1] # 1
sol.findClosestNumber(nums)
assert sol.findClosestNumber(nums) == 1