from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_ptr = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_ptr]:
                unique_ptr += 1
                nums[unique_ptr] = nums[i]

        return unique_ptr + 1