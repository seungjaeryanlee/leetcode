"""
Solution for July LeetCoding Challenges Week 1 Day 1: Arranging Coins
"""
import math


class Solution1:
    """
    Naively count coins row by row until there is not enough rows

    - Number of coins : N
    - Space Complexity: O(1)
    - Time Complexity: O(log N)

    Runtime: 984 ms / 33.65%
    Memory Usage: 13.9 MB / 29.09%
    """
    def arrangeCoins(self, n: int) -> int:
        used_coins = 0
        for row in range(1, n+2): # Need +2 for n == 1
            # Not enough coins
            if n - used_coins < row:
                return row - 1
            # Count used coins
            used_coins += row

        # Should never reach this except when n < 0
        return -1


class Solution2:
    """
    Count down from sqrt(N) since row(row+1)/2 <= n, so row <= sqrt(2n)

    - Number of coins : N
    - Space Complexity: O(1)
    - Time Complexity: ?

    Runtime: 36 ms / 72.91%
    Memory Usage: 14 MB / 13.25%
    """
    def arrangeCoins(self, n: int) -> int:
        for row in range(int(math.sqrt(2 * n)), -1 , -1):
            if row * (row + 1) / 2 <= n:
                return row

        # Should never reach this except when n < 0
        return -1
