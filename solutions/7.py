class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        reversed_x_str = x_str[::-1]

        if reversed_x_str[-1] == '-':
            reversed_x = -1 * int(reversed_x_str[:-1])
        else:
            reversed_x = int(reversed_x_str)

        if reversed_x < - (2 ** 31) or reversed_x > 2 ** 31 - 1:
            return 0
        else:
            return reversed_x
