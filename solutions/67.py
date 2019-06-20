"""
Solution for Algorithms #67: Add Binary.

- N: Maximum of lengths of `a` and `b`
- Space Complexity: O(N)
- Time Complexity: O(N)

Runtime: 40 ms, faster than 79.48% of Python3 online submissions for Add Binary.
Memory Usage: 13.2 MB, less than 42.91% of Python3 online submissions for Add Binary.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Edge case
        if a == '0' and b == '0': return '0'

        a = list(a[::-1])
        b = list(b[::-1])

        reversed_total = ''
        carry = 0
        while a or b:
            digit_total = int(a[0] if a else '0') + int(b[0] if b else '0') + carry
            if digit_total == 3:
                carry = 1
                reversed_total += '1'
            elif digit_total == 2:
                carry = 1
                reversed_total += '0'
            elif digit_total == 1:
                carry = 0
                reversed_total += '1'
            else:
                carry = 0
                reversed_total += '0'

            if a: del a[0]
            if b: del b[0]

        if carry:
            reversed_total += '1'

        return reversed_total[::-1]