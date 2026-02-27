class Solution1:
    def maxSubArray(self, nums: list[int]) -> int:
        max_num = max(nums)
        if max_num < 0:
            return max_num

        output = 0
        current = 0
        for num in nums:
            current += num
            if current < 0:
                current = 0
            output = max(output, current)

        return output

class Solution2:
    def recursion(self, nums: list[int], left: int, right: int) -> tuple[int, int, int, int]:
        print(left, right)
        if left == right:
            return nums[left], nums[left], nums[left], nums[left]
        middle = (left + right) // 2
        
        left_total, left_prefix, left_suffix, left_best = self.recursion(nums, left, middle)
        right_total, right_prefix, right_suffix, right_best = self.recursion(nums, middle+1, right)

        return (
            left_total + right_total,
            max(left_prefix, left_total+right_prefix),
            max(right_suffix, right_total+left_suffix),
            max(left_best, right_best, left_suffix + right_prefix),
        )

    def maxSubArray(self, nums: list[int]) -> int:
        return self.recursion(nums, 0, len(nums)-1)[3]