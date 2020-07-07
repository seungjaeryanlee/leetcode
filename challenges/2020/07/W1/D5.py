"""
Solution for July LeetCoding Challenges Week 1 Day 5: Hamming Distance
"""
class Solution1:
    """
    Assumes no bitwise operation.

    - Space Complexity: O(1)
    - Time Complexity: O(log min(x, y))
      - O(1) if x, y is bounded

    Runtime: 32 ms / 70.36%
    Memory Usage: 13.8 MB / 69.69%
    """
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        while x or y:
            distance += x % 2 != y % 2
            x = x // 2
            y = y // 2

        return distance


class Solution3:
    """
    Use bit operations.

    - Space Complexity: O(1)
    - Time Complexity: O(log min(x, y))
      - O(1) if x, y is bounded

    Runtime: 36 ms / 50.95%
    Memory Usage: 14 MB / 19.53%
    """
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            if xor & 1:
                distance += 1
            xor >>= 1

        return distance


class Solution3:
    """
    Use Brian Kernighan's bit counting algorithm.

    NOTE(seungjaeryanlee): This is copied from the reference solution.

    - Number of 1s: K
    - Space Complexity: O(1)
    - Time Complexity: O(K)
      - O(1) if x, y is bounded

    Runtime: 36 ms / 50.95%
    Memory Usage: 13.7 MB / 89.98%
    """
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            xor = xor & (xor - 1)

        return distance
