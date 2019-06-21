"""
Solution for Algorithms #268: Missing Number

- N: Length of `nums`
- Space Complexity: O(1)
- Time Complexity: O(N)

Runtime: 40 ms, faster than 93.94% of Python3 online submissions for Missing Number.
Memory Usage: 13.8 MB, less than 99.30% of Python3 online submissions for Missing Number.
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (1 + len(nums)) * len(nums) // 2 - sum(nums)
