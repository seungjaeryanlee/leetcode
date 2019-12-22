"""
Solution for Algorithms #125: Valid Palindrome

- N: Length of string
- Space Complexity: O(1)
- Time Complexity: O(N)

Runtime: 44 ms, faster than 86.53% of Python3 online submissions for Valid Palindrome.
Memory Usage: 13.1 MB, less than 97.62% of Python3 online submissions for Valid Palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
                left += 1
            elif s[right] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True
