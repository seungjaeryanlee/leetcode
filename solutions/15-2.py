"""
Solution for Algorithms #15: 3Sum

I wrote this solution after reading 
https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)

Runtime: 2896 ms, faster than 15.49% of Python3 online submissions for 3Sum.
Memory Usage: 16.8 MB, less than 20.16% of Python3 online submissions for 3Sum.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []

        nums = sorted(nums)
        for i, n1 in enumerate(nums):
            if n1 > 0: break
            # Don't check if this number has been checked already with duplicates
            if i > 0 and nums[i-1] == n1: continue

            left_i = i+1
            right_i = len(nums)-1

            while left_i < right_i:
                total = n1 + nums[left_i] + nums[right_i]
                if total == 0:
                    if [n1, nums[left_i], nums[right_i]] not in solutions:
                        solutions.append([n1, nums[left_i], nums[right_i]])

                    # Skip duplicates for left_i and right_i
                    while left_i < right_i and nums[left_i] == nums[left_i + 1]:
                        left_i += 1
                    while left_i < right_i and nums[right_i - 1] == nums[right_i]:
                        right_i -= 1
                    left_i += 1
                    right_i -= 1
                elif total > 0:
                    right_i -= 1
                else:
                    left_i += 1

        return solutions
