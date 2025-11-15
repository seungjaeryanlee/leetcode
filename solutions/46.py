"""
Runtime: 0 ms, faster than 100.00%
Memory Usage: 17.85 MB, less than 82.60%
"""
from typing import List


class Solution:
    def step(self, current: List[int], nums: List[int]):
        if not nums:
            return [current]

        results = []
        for i, num in enumerate(nums):
            new_current = current + [num]
            new_nums = nums[:i] + nums[i+1:]
            results.extend(self.step(new_current, new_nums))
        
        return results

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.step([], nums)