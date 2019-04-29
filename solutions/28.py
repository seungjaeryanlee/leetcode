"""
Solution for Algorithms #28: Implement strStr()

Runtime: 36 ms, faster than 88.85% of Python3 online submissions for Implement strStr().
Memory Usage: 13.4 MB, less than 5.13% of Python3 online submissions for Implement strStr().
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Implementing from scratch for practice
        if len(haystack) < len(needle):
            return -1
        if len(needle) == 0:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
