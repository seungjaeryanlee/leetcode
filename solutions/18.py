"""
Solution for Algorithms #18: 4Sum

TODO This is O(N^3). Looks like the discussion forum is talking about O(N^2) solution?

Runtime: 740 ms, faster than 47.91% of Python3 online submissions for 4Sum.
Memory Usage: 13.4 MB, less than 16.60% of Python3 online submissions for 4Sum.
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        solutions = []

        for i, n1 in enumerate(nums):
            # If n1 > target and any of n2, n3, n4 >= 0, total > target.
            # If n1 >= target and any of n2, n3, n4 > 0, total > target.
            if n1 >= 0 and n1 > target or n1 > 0 and n1 >= target:
                # Next n1 candidates will be bigger, so we can break
                break
            for j, n2 in enumerate(nums[i+1:], i+1):
                if n2 >= 0 and n1 + n2 > target or n2 > 0 and n1 + n2 >= target:
                    break

                left_i = j+1
                right_i = len(nums) - 1

                while left_i < right_i:
                    total = n1 + n2 + nums[left_i] + nums[right_i]
                    if total < target:
                        left_i += 1
                    elif total > target:
                        right_i -= 1
                    else: # total == target
                        # TODO Below if is not needed?
                        if [n1, n2, nums[left_i], nums[right_i]] not in solutions:
                            solutions.append([n1, n2, nums[left_i], nums[right_i]])

                        # Change indices
                        left_i += 1
                        right_i -= 1
                        # If new left and right are same as old left and right, change again
                        while left_i < right_i and nums[left_i-1] == nums[left_i]:
                            left_i += 1
                        while left_i < right_i and nums[right_i] == nums[right_i+1]:
                            right_i -= 1

        return solutions
