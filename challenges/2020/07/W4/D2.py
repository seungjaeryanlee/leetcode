"""
Solution for July LeetCoding Challenges Week 4 Day 2: Single Number III
"""
class Solution:
    """
    Keep a dictionary of numbers, adding keys on first occurence and removing
    keys on second occurence.

    Space : O(N)
    ----------------
    counter : O(N)
        N is the size of the input nums. In the worst case, around half of the
        numbers need to be stored in the dictionary.

    Time : O(N)
    -----------
    counter : O(N)
        All N numbers must be checked.

    Runtime: 60 ms / 84.24%
    Memory Usage: 15.9 MB / ?
    """
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                del counter[num]
        return counter.keys()
