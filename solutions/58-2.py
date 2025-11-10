"""
Runtime: 0 ms, beats 100.00%.
Memory Usage: 17.92 MB, beats 17.15%
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for c in s[::-1]:
            if c == " ":
                if count > 0:
                    return count
            else:
                count += 1
        
        return count
