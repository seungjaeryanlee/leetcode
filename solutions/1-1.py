"""
Time Limit Exceeded
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Method 1: Brute force
        # Space: O(1)
        # Time: O(N^2)
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i >= j: continue
                if n1 + n2 == target:
                    return [i, j]
