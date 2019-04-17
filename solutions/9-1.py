"""
Solution for Algorithms #9: Palindrome Number.

Runtime: 76 ms, faster than 100.00% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.1 MB, less than 5.03% of Python3 online submissions for Palindrome Number.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Method 1: Convert to string
        x_str = str(x)
        return x_str == x_str[::-1]
