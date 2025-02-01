from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate the current area
            current_area = (right - left) * min(height[left], height[right])
            # Update max_area if the current area is greater
            if current_area > max_area:
                max_area = current_area

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
        
height = [1,8,6,2,5,4,8,3,7]

solution = Solution()
print(solution.maxArea(height))