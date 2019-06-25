"""
Naive solution for Algorithm #69: Sqrt(x)
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x, -1, -1):
            if i ** 2 <= x:
                return i
