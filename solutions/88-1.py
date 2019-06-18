"""
Naive solution for Algorithms #88: Merge Sorted Array.

- N: len(nums1)
- M: len(nums2)
- Space Complexity: O(1)
- Time Complexity: O(MN)
  - Shifting takes O(N) time, and this could occur O(M) times

Runtime: 60 ms, faster than 8.53% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.3 MB, less than 18.88% of Python3 online submissions for Merge Sorted Array.
"""
class Solution:
    def _shift_and_insert(self, arr, position, value):
        for i in range(len(arr)-2, position-1, -1):
            arr[i+1] = arr[i]
        arr[position] = value

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2 = 0, 0
        while i1 < m+n and i2 < n:
            if nums1[i1] > nums2[i2]:
                self._shift_and_insert(nums1, i1, nums2[i2])
                i2 += 1
            else: i1 += 1
        for j in range(i2, n):
            nums1[m+j] = nums2[j]
