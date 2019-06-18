"""
Solution for Algorithms #121: Best Time to Buy and Sell Stock.

- N: Number of prices
- Space Complexity: O(1)
- Time Complexity: O(N)

Runtime: 32 ms, faster than 99.07% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.9 MB, less than 60.94% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0

        max_profit = 0
        lowest_point = prices[0]
        for price in prices[1:]:
            if price - lowest_point > max_profit:
                max_profit = price - lowest_point
            if price < lowest_point:
                lowest_point = price

        return max_profit
