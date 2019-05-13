"""
Solution for Algorithms #34: Find First and Last Position of Element in Sorted Array

Method:
1. Find one instance `instance_i` of target in array with binary search.
  - Save last known (left, right) pair to accelerate steps 2, 3
2. Find the leftmost instance of target with binary search.
  - Search from (known_left, instance_i)
3. Find the rightmost instance of target with binary search.
  - Search from (instance_i, known_right)

Runtime: 32 ms, faster than 99.85% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 13.7 MB, less than 5.06% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 1) Find one instance
        left, right = 0, len(nums) - 1
        instance_i = -1

        while left <= right:
            middle = int((left + right)/2)

            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else: # nums[middle] == target
                instance_i = middle
                break

        # No instance found
        if instance_i == -1:
            return [-1, -1]

        # These (left, right) pairs have nice property that
        # nums[:left] < target and nums[right+1:] > target.
        known_left, known_right = left, right

        # 2) Find leftmost instance
        left, right = known_left, instance_i
        leftmost_i = instance_i

        while left <= right:
            middle = int((left + right)/2)

            if nums[middle] < target:
                left = middle + 1
            else: # nums[middle] == target
                leftmost_i = middle
                right = middle - 1

        # 3) Find rightmost instance
        left, right = instance_i, known_right
        rightmost_i = instance_i

        while left <= right:
            middle = int((left + right)/2)

            if nums[middle] > target:
                right = middle - 1
            else: # nums[middle] == target
                rightmost_i = middle
                left = middle + 1

        return [leftmost_i, rightmost_i]
