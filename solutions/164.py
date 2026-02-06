
from collections import defaultdict
import math
from dataclasses import dataclass


class Solution1:
    """
    Naive solution using built-in sort, which has O(n log n) time complexity.
    """
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0

        sorted_nums = sorted(nums)

        max_gap = 0
        for i, num in enumerate(sorted_nums):
            if i == 0:
                continue
            prev_num = sorted_nums[i-1]
            max_gap = max(max_gap, num - prev_num)
        
        return max_gap
    

class Solution2:
    """
    Implement radix sort instead of built-in sort to achieve O(n) time complexity.
    """
    def radix_sort_recursion(self, nums: list[int], level: int) -> list[int]:
        digit_to_list = defaultdict(list)
        for num in nums:
            digit = (num // (10 ** level)) % 10
            digit_to_list[digit].append(num)

        output = []
        for i in range(10):
            if not digit_to_list[i]:
                continue
            if level > 0:
                output += self.radix_sort_recursion(digit_to_list[i], level-1)
            else:
                output.extend(digit_to_list[i])

        return output

    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0

        max_level = 0 if max(nums) == 0 else int(math.log10(max(nums)))
        sorted_nums = self.radix_sort_recursion(nums, max_level)

        max_gap = 0
        for i, num in enumerate(sorted_nums):
            if i == 0:
                continue
            prev_num = sorted_nums[i-1]
            max_gap = max(max_gap, num - prev_num)
        
        return max_gap
    

@dataclass
class Bucket:
    min: int | None
    max: int | None

    def is_empty(self):
        return self.min is None and self.max is None

    def add(self, num):
        self.min = min(self.min, num) if self.min is not None else num
        self.max = max(self.max, num) if self.max is not None else num

class Solution3:
    """
    Bucket sort solution, which has O(n) time complexity.
    The idea is to create buckets of a certain size, and then assign numbers to these buckets.
    The maximum gap will be between the maximum of one bucket and the minimum of the next non-empty bucket.
    """
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0

        # Step 0: Prepare
        min_nums = min(nums)
        max_nums = max(nums)
        len_nums = len(nums)

        if max_nums == min_nums:
            return 0

        # Step 1: Create maximum bucket size so that max gap must be between two buckets
        n_gaps = len_nums - 1
        min_solution = (max_nums - min_nums) / n_gaps
        bucket_size = math.ceil(min_solution)
        if bucket_size < 1:
            bucket_size = 1
        
        # Step 2: Assign nums to buckets
        bucket_count = (max_nums - min_nums) // bucket_size + 1
        bucket_to_nums = [Bucket(min=None, max=None) for _ in range(bucket_count)]
        for num in nums:
            bucket = (num - min_nums) // bucket_size
            bucket_to_nums[bucket].add(num)

        # Step 3. Go through buckets
        max_gap = 0
        prev_bucket = bucket_to_nums[0] # Guaranteed non-empty as it contains min
        for bucket in bucket_to_nums[1:]:
            if bucket.is_empty():
                continue

            new_gap = bucket.min - prev_bucket.max
            max_gap = max(max_gap, new_gap)
            prev_bucket = bucket
        
        return max_gap