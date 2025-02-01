from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to avoid duplicates
        result = []
        
        for i in range(len(nums) - 2):  # Iterate up to the third-to-last element
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the fixed element
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # Move left pointer to increase the sum
                elif total > 0:
                    right -= 1  # Move right pointer to decrease the sum
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move pointers to the next unique elements
                    left += 1
                    right -= 1
        
        return result

nums = [-1,0,1,2,-1,-4]
solution = Solution()
print(solution.threeSum(nums))