"""
Solution for Algorithms #16: 3Sum Closest

Runtime: 76 ms, faster than 96.50% of Python3 online submissions for 3Sum Closest.
Memory Usage: 13.2 MB, less than 5.29% of Python3 online submissions for 3Sum Closest.
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest_total = sum(nums[0:3])

        for i, n1 in enumerate(nums):
            # Adding n2 or n3 will increase offset
            if n1 >= closest_total > target and n1 >= 0:
                break

            for j, n2 in enumerate(nums[i+1:], i+1):
                # Adding n3 will increase offset
                if n1 + n2 >= closest_total > target and n2 >= 0:
                    break

                left_i = j+1
                right_i = len(nums)-1

                # Below 4 lines makes change 792ms to 76ms
                offset = abs(closest_total - target)
                if left_i > right_i: break
                if n1 + n2 + nums[left_i] > target + offset: break
                if n1 + n2 + nums[right_i] < target - offset: break

                while left_i <= right_i:
                    middle_i = int((left_i + right_i) / 2)
                    total = n1 + n2 + nums[middle_i]

                    # TODO Can we break sometime?
                    if abs(closest_total - target) > abs(total - target):
                        closest_total = total

                    if target < total:
                        right_i = middle_i - 1
                    elif target > total:
                        left_i = middle_i + 1
                    else:
                        return target

        return closest_total
