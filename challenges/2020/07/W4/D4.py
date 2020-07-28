"""
Solution for July LeetCoding Challenges Week 4 Day 4: Find Minimum in Rotated Sorted Array II
"""
class Solution:
    """
    Go through the list and check if the number suddenly decreases. Return the
    decreased number if it happens, otherwise the list is sorted, so return
    the first element.

    Space : O(1)
    ------------
    Nothing taking up space other than a few variables.

    Time : O(N)
    -----------
    N is the length of the list. If the list is sorted, the entire list must be
    checked.

    Runtime: 100 ms / 8.34%
    Memory Usage: 14.4 MB / 10.55%
    """
    def findMin(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i < len(nums) - 1 and num > nums[i+1]:
                return nums[i+1]
        return nums[0]
