"""
Solution for Algorithms #29: Divide Two Integers.

Runtime: 40 ms, faster than 100.00% of Python3 online submissions for Divide Two Integers.
Memory Usage: 13.4 MB, less than 5.26% of Python3 online submissions for Divide Two Integers.
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = int(abs(dividend) / abs(divisor))
        result = result if dividend * divisor > 0 else -result

        return result if -(2**31) <= result <= 2**31 - 1 else 2**31 - 1
