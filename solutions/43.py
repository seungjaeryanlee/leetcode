"""
Solution for Algorithms #43: Multiply Strings

Runtime: 192 ms, faster than 22.79% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.3 MB, less than 29.32% of Python3 online submissions for Multiply Strings.
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Digits of product in reversed order
        reversed_total = [0] * (len(num1) + len(num2))

        # Mutiply digit-by-digit
        for i, c1 in enumerate(num1):
            for j, c2 in enumerate(num2):
                digit_product = int(c1) * int(c2)
                reversed_index = (len(num1)-i-1) + (len(num2)-j-1)
                if digit_product >= 10:
                    reversed_total[reversed_index] += digit_product % 10
                    reversed_total[reversed_index+1] += int(digit_product / 10)
                else:
                    reversed_total[reversed_index] += digit_product

        # Carry
        for i, digit in enumerate(reversed_total):
            if digit >= 10:
                reversed_total[i] = digit % 10
                reversed_total[i+1] += int(digit / 10)

        # Remove zeros
        while reversed_total[-1] == 0:
            del reversed_total[-1]

        total = list(reversed(reversed_total))
        return ''.join(str(digit) for digit in total)
