"""
Runtime: 44 ms, faster than 92.32% of Python3 online submissions for Two Sum.
Memory Usage: 14.2 MB, less than 56.28% of Python3 online submissions for Two Sum.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Method 3: Hash the difference
        # key: num
        # value: index of num
        # Space: O(N)
        # Time: O(N)
        num_to_id = {}
        for i, num in enumerate(nums):
            if target - num in num_to_id:
                return [i, num_to_id[target - num]]
            else:
                num_to_id[num] = i
