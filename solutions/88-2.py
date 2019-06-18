"""
Better solution for Algorithms #88: Merge Sorted Array.

- N: len(nums1)
- M: len(nums2)
- Space Complexity: O(1)
- Time Complexity: O(N + M)

Runtime: 52 ms, faster than 17.43% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13 MB, less than 87.25% of Python3 online submissions for Merge Sorted Array.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2 = m-1, n-1
        while i1 >= 0 and i2 >= 0:
            if nums2[i2] >= nums1[i1]:
                nums1[i1+i2+1] = nums2[i2]
                i2 -= 1
            else:
                nums1[i1+i2+1] = nums1[i1]
                i1 -= 1
        for j in range(0, i2+1):
            nums1[j] = nums2[j]
