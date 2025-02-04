from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        bot = 0
        top = len(nums)-1

        while bot <= top:
            mid = bot + (top - bot) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                bot = mid +1
            else: top = mid -1
        return bot
