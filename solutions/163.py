from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]

        output = []
        next_lower = lower
        for num in nums:

            if num <= next_lower:
                next_lower += 1
                continue
            if num > upper:
                output.append([next_lower, upper])
                break
            
            output.append([next_lower, num-1])
            next_lower = num + 1
        
        if nums and nums[-1] < upper:
            output.append([nums[-1] + 1, upper])

        return output
