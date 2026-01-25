class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        output = -1
        nums = sorted(nums)
        for i in range(len(nums) // 2 + 1):
            output = max(output, nums[i] + nums[len(nums)-1-i])

        return output