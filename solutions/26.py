"""
Solution for Algorithms #26: Remove Duplicates from Sorted Array

Runtime: 76 ms, faster than 37.87% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.8 MB, less than 5.43% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                del nums[i]
            else:
                i += 1

        return i
