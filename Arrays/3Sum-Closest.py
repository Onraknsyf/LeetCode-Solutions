from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array to make it easier to find the closest sum
        closest_sum = float('inf')  # Initialize with a large value
        
        for i in range(len(nums) - 2):  # Iterate up to the third-to-last element
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update the closest sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on the comparison with the target
                if current_sum < target:
                    left += 1  # Move left pointer to increase the sum
                elif current_sum > target:
                    right -= 1  # Move right pointer to decrease the sum
                else:
                    # If the sum is exactly equal to the target, return it immediately
                    return current_sum
        
        return closest_sum