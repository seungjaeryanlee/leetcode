"""
Solution for Algorithms #238: Product of Array Except Self.

- N: Length of `nums`
- Space Complexity: O(N)
- Time Complexity: O(N)

Runtime: 112 ms, faster than 32.74% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 20.5 MB, less than 77.34% of Python3 online submissions for Product of Array Except Self.
"""
from collections import deque


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = []
        right_products = []

        last_left_product = 1
        for i in range(0, len(nums)):
            left_products.append(last_left_product)
            last_left_product *= nums[i]

        last_right_product = 1
        for i in range(len(nums)-1, -1, -1):
            right_products.append(last_right_product)
            last_right_product *= nums[i]
        right_products = right_products[::-1]

        return [left * right for left, right in zip(left_products, right_products)]
