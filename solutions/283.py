"""
Solution for Algorithms #283: Move Zeroes.

- N: Length of `nums`.
- Space Complexity: O(1)
- Time Complexity: O(N)

Runtime: 48 ms, faster than 86.25% of Python3 online submissions for Move Zeroes.
Memory Usage: 14.3 MB, less than 87.87% of Python3 online submissions for Move Zeroes.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i, num in enumerate(nums):
            if num != 0:
                if i != j: nums[j] = num
                j += 1
        for k in range(j, len(nums)):
            nums[k] = 0
