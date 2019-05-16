"""
Solution for Algorithms #35: Search Insert Position

Runtime: 32 ms, faster than 99.12% of Python3 online submissions for Search Insert Position.
Memory Usage: 13.8 MB, less than 19.42% of Python3 online submissions for Search Insert Position.
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if target < nums[left]: return left
            if target > nums[right]: return right + 1

            middle = int((left + right) / 2)
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle

        # Not found
        return left + 1
