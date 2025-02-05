from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        first, second = 0,1

        while second < len(nums):
            if nums[first] == nums[second]:
                return nums[first]
            first += 1
            second += 1