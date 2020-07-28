"""
Solution for July LeetCoding Challenges Week 4 Day 5: Add Digits
"""
class Solution:
    """
    Repeat until the number is less than 10.

    Space : O(1)
    ------------
    Nothing taking up space other than a few variables.

    Time : ?
    -----------
    Difficult to determine.

    Runtime: 24 ms / 97.30%
    Memory Usage: 13.5 MB / 99.60%
    """
    def step(self, num: int) -> int:
        new_num = sum(int(c) for c in str(num))
        return new_num

    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = self.step(num)
        return num
