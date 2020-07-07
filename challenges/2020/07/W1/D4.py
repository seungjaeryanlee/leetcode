"""
Solution for July LeetCoding Challenges Week 1 Day 4: Ugly Number II
"""
import heapq


class Solution:
    """
    Uses a min heap.

    - n: N
    - Space Complexity: O(N)
    - Time Complexity: O(N log N)

    Runtime: 1296 ms / 7.80%
    Memory Usage: 13.8 MB / 81.77%
    """
    def nthUglyNumber(self, n: int) -> int:
        min_heap = [1]
        heapq.heapify(min_heap)

        for _ in range(n):
            elem = heapq.heappop(min_heap)
            for new_elem in [elem*2, elem*3, elem*5]:
                if new_elem not in min_heap:
                    heapq.heappush(min_heap, new_elem)

        return elem
