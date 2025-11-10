"""
Runtime: 0 ms, beats 100.00%.
Memory Usage: 17.82 MB, beats 37.54%
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
