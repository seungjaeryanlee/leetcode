"""
Solution for Algorithms #27: Remove Element

Runtime: 36 ms, faster than 99.37% of Python3 online submissions for Remove Element.
Memory Usage: 13.1 MB, less than 5.09% of Python3 online submissions for Remove Element.
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                del nums[i]

        return len(nums)
