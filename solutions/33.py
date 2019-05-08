"""
Solution for Algorithms #33: Search in Rotated Sorted Array

Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 13.4 MB, less than 5.96% of Python3 online submissions for Search in Rotated Sorted Array.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## General Idea
        # Split in middle, check leftmost (l), middle (m), rightmost (r)
        # if n[l] < n[m] > n[r], pivot exists in [m, r].
        # if n[l] < target < n[m], search from [l, m]
        # if target > n[m] or target < n[l], search [m, r]
        # Same rule applies when n[l] > n[m] < n[r].

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = int((left + right) / 2)
            if nums[left] == target: return left
            if nums[right] == target: return right
            if nums[middle] == target: return middle

            if nums[left] < nums[middle] and nums[right] < nums[middle]:
                # Pivot exists in [m, r]
                if nums[left] < target < nums[middle]: # Left side
                    left = left + 1
                    right = middle - 1
                else: # Right side
                    left = middle + 1
                    right = right - 1
            else:
                # Pivot exists in [l, m]
                if nums[middle] < target < nums[right]: # Right side
                    left = middle + 1
                    right = right - 1
                else: # Left side
                    left = left + 1
                    right = middle - 1

        return -1
