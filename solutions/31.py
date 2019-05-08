"""
Solution for Algorithms #31: Next Permutation

Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Next Permutation.
Memory Usage: 13.2 MB, less than 5.24% of Python3 online submissions for Next Permutation.
"""
class Solution:
    def reverse_sublist(self, nums, start, end):
        """
        Reverse order of sublist from start to end (both inclusive indices).
        """
        if start == end: return
        for i in range(int((end-start+1)/2)):
            nums[start+i], nums[end-i] = nums[end-i], nums[start+i]

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                self.reverse_sublist(nums, i, len(nums)-1)
                for j in range(i, len(nums)):
                    if nums[i-1] < nums[j]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        break
                return

        # If here, nums is sorted in decreasing order
        nums.reverse()
