"""
Runtime: 72 ms, faster than 99.89% of Python3 online submissions for Single Number.
Memory Usage: 15.2 MB, less than 18.03% of Python3 online submissions for Single Number.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Space: O(N)
        # Time: O(N)
        odds = {}
        for num in nums:
            if num not in odds:
                odds[num] = True
            else:
                del odds[num]

        return list(odds.keys())[0]
