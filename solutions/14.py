"""
Solution for Algorithms #14: Longest Common Prefix

Runtime: 40 ms, faster than 73.32% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.3 MB, less than 5.10% of Python3 online submissions for Longest Common Prefix.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        prefix = ''
        for i, c in enumerate(strs[0]):
            for s in strs:
                if len(s) <= i or s[i] != c:
                    return prefix
            prefix += c

        return prefix
