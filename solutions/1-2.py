"""
Runtime: 68 ms, faster than 35.76% of Python3 online submissions for Two Sum.
Memory Usage: 14.5 MB, less than 30.23% of Python3 online submissions for Two Sum.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Method 2: Sort and two pointers
        # Space: O(N)
        # Time: O(N log N)
        nums_with_ids = enumerate(nums)
        sorted_nums_with_ids = sorted(nums_with_ids, key=lambda x: x[1])
        i, j = 0, len(nums) - 1
        while i < j:
            print(i, j)
            if sorted_nums_with_ids[i][1] + sorted_nums_with_ids[j][1] > target:
                j -= 1
            elif sorted_nums_with_ids[i][1] + sorted_nums_with_ids[j][1] < target:
                i += 1
            else:
                return [sorted_nums_with_ids[i][0], sorted_nums_with_ids[j][0]]
