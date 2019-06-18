"""
Solution for Algorithms #238: Product of Array Except Self.

- N: Length of `nums`
- Space Complexity: O(1)
  - Excluding the output array
- Time Complexity: O(N)

Runtime: 92 ms, faster than 98.49% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 20.8 MB, less than 11.10% of Python3 online submissions for Product of Array Except Self.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []

        last_left_product = 1
        for i in range(0, len(nums)):
            products.append(last_left_product)
            last_left_product *= nums[i]

        last_right_product = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= last_right_product
            last_right_product *= nums[i]

        return products
