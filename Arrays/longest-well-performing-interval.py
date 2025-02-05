from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        l, r = 0, 0
        longest = 0
        
        while r < len(hours):
            tiring_days = 0
            non_tiring_days = 0

            for i in range(l, r + 1):
                if hours[i] > 8:
                    tiring_days += 1
                else:
                    non_tiring_days += 1

            if tiring_days > non_tiring_days:
                longest = max(longest, r - l + 1)
            
            r += 1

            if r == len(hours) and l < len(hours) - 1:
                l += 1
                r = l

        return longest
