"""
Solution for Algorithms #78: Subsets

- N: Length of `nums`
- Space Complexity: O(2^N)
- Time Complexity: ?

Runtime: 44 ms, faster than 65.14% of Python3 online submissions for Subsets.
Memory Usage: 13.2 MB, less than 74.91% of Python3 online submissions for Subsets.
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = [[]]
        for num in nums:
            # By doing this, `power_set` contains one set without `num` and one set with `num`
            power_set += [item+[num] for item in power_set]

        return power_set
