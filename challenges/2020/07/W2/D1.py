"""
Solution for July LeetCoding Challenges Week 2 Day 1: 3Sum
"""
class Solution1:
    """
    Sort and check all {N choose 3} combinations

    - Length of nums : N
    - Length of output: K
    - Space Complexity: O(log N) (assuming Quicksort)
    - Time Complexity: O(N^3 K)

    Time Limit Exceeded
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []

        # Assume in-place is allowed
        nums.sort()
        print(nums)
        
        output = []
        for i in range(len(nums)):
            if 3 * nums[i] > 0:
                break
            for j in range(i+1, len(nums)):
                if nums[i] + 2 * nums[j] > 0:
                    break
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] > 0:
                        break
                    if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in output:
                        output.append([nums[i], nums[j], nums[k]])
        
        return output


class Solution2:
    """
    Reduce to N 2Sum problems

    This solution was created after reading the first hint:
        So, we essentially need to find three numbers x, y, and z such that they add up to the given value. If we fix one of the numbers say x, we are left with the two-sum problem at hand!

    - Length of nums : N
    - Length of output: K
    - Space Complexity: O(log N) (assuming Quicksort)
    - Time Complexity: O(N^2 K)

    Time Limit Exceeded
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []

        # Assume in-place is allowed
        nums.sort()
        print(nums)
        
        output = []
        for i in range(len(nums)):
            if 3 * nums[i] > 0:
                break
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    # TODO: Probably can be improved
                    if [nums[i], nums[left], nums[right]] not in output:
                        output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

        return output


class Solution3:
    """
    Solution 2, but remove checking for duplicates

    - Length of nums : N
    - Length of output: K
    - Space Complexity: O(log N) (assuming Quicksort)
    - Time Complexity: O(N^2)

    Runtime: 1104 ms / 55.13%
    Memory Usage: 17.2 MB / 62.34%
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []

        # Assume in-place is allowed
        nums.sort()
        print(nums)
        
        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if 3 * nums[i] > 0:
                break
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    while right > 0 and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                elif total < 0:
                    while left < len(nums) - 1 and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    while left < len(nums) - 1 and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    while right > 0 and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1

        return output
