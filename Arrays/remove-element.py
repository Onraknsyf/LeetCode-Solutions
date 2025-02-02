from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for i in range(len(nums)):
            if (val != nums[i]):
                nums[counter] = nums[i]
                counter += 1
        return counter
    
nums = [0,1,2,2,3,0,4,2]
target = 2
solution = Solution()
print(solution.removeElement(nums, target))