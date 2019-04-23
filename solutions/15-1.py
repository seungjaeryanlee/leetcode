"""
Solution for Algorithms #15: 3Sum

I get 'Time Limit Exceeded' for this O(N^2 log N) solution.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []

        sorted_nums = sorted(nums)
        for i, n1 in enumerate(sorted_nums):
            if n1 > 0:
                break
            for j, n2 in enumerate(sorted_nums[i+1:], i+1):
                if n1 + n2 > 0:
                    break
                # Binary search -(n1 + n2) from sorted_nums[j+1:]
                left_i = j+1
                right_i = len(sorted_nums)-1
                while left_i <= right_i:
                    middle_i = int((left_i + right_i) / 2)
                    if n1 + n2 + sorted_nums[middle_i] == 0:
                        # Check duplicate
                        if [n1, n2, sorted_nums[middle_i]] not in solutions:
                            solutions.append([n1, n2, sorted_nums[middle_i]])
                        break
                    elif n1 + n2 + sorted_nums[middle_i] > 0:
                        right_i = middle_i - 1
                    else:
                        left_i = middle_i + 1

        return solutions
