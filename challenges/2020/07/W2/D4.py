"""
Solution for July LeetCoding Challenges Week 2 Day 4: Subsets
"""
class Solution:
    """
    Double the set iteratively

    - Number of nodes: N
    - Space Complexity: O(N 2^N)
    - Time Complexity: O(N 2^N)

    Runtime: 32 ms / 86.44%
    Memory Usage: 14 MB / 60.80%
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = [[]]
        for num in nums:
            # By doing this, `power_set` contains one set without `num` and one set with `num`
            power_set += [item+[num] for item in power_set]

        return power_set
