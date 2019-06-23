"""
Solution for Algorithms #344 (Reverse String)

- Space Complexity: O(1)
- Time Complexity: O(N)

Runtime: 176 ms, faster than 45.30% of Python3 online submissions for Reverse String.
Memory Usage: 17.7 MB, less than 36.68% of Python3 online submissions for Reverse String.
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
