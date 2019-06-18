"""
Weird but efficient solution for Algorithms #88: Merge Sorted Array.

- N: len(nums1)
- M: len(nums2)
- Space Complexity: O(1)
- Time Complexity: O(MN)

Runtime: 52 ms, faster than 17.43% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13 MB, less than 87.25% of Python3 online submissions for Merge Sorted Array.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = m-1
        while i1 >= 0 and nums2:
            if nums2[-1] >= nums1[i1]:
                nums1[i1+len(nums2)] = nums2[-1]
                del nums2[-1]
            else:
                nums1[i1+len(nums2)] = nums1[i1]
                i1 -= 1
        for j, n in enumerate(nums2):
            nums1[j] = n
