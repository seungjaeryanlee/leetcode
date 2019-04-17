"""
Solution for Algorithms #9: Palindrome Number.

Runtime: 132 ms, faster than 78.47% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.1 MB, less than 5.03% of Python3 online submissions for Palindrome Number.
"""
import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Method 2: No-string restriction
        if x < 0:
            return False
        if x == 0:
            return True

        reconstructed_x = 0
        nb_digits = math.floor(math.log10(abs(x))) + 1

        copied_x = x
        for i in range(math.floor(nb_digits/2)):
            next_digit = copied_x % 10
            factor = 10 ** ((nb_digits-1) - i) + 10 ** i
            reconstructed_x += next_digit * factor
            copied_x = math.floor(copied_x / 10)

        # If odd-length, add middle:
        if nb_digits % 2 == 1:
            reconstructed_x += math.floor(x / 10 ** math.floor(nb_digits/2)) % 10 * 10 ** math.floor(nb_digits/2)

        return x == reconstructed_x
