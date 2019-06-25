"""
Binary Search solution for Algorithm #69: Sqrt(x)

- N: Range of x
- Time Complexity: O(log N)
- Space Complexity: O(1)

Runtime: 44 ms, faster than 66.52% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.2 MB, less than 53.88% of Python3 online submissions for Sqrt(x).
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        # Assumes that 0 <= x <= 2^31 - 1
        start, end = 0, 65536

        while start + 1 < end:
            base = (start + end) // 2
            if x == base ** 2:
                return base
            elif x > base ** 2:
                start = base
            else: # x < base ** 2:
                end = base

        if end ** 2 <= x:
            return end
        else:
            return start
