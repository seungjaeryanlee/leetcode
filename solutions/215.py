"""
Heap Solution for Algorithms #215 (Kth Largest Element in an Array).

- N: len(nums), K: k
- Space Complexity: O(K)
- Time Complexity: O(NK log K)
  - Heap push/pop operation: O(K log K)

Runtime: 52 ms, faster than 40.26% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 13.8 MB, less than 31.07% of Python3 online submissions for Kth Largest Element in an Array.
"""

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums[:k]:
            heapq.heappush(h, num)
        for num in nums[k:]:
            heapq.heappushpop(h, num)

        return h[0]
