"""
More efficient solution for Algorithms #56: Merge Intervals

- N: Number of intervals
- Space Complexity: O(N)
  - Assumes that we can modify given `intervals` list.
- Time Complexity: O(N log N)
  - Sorting intervals takes O(N log N)

Runtime: 52 ms, faster than 71.88% of Python3 online submissions for Merge Intervals.
Memory Usage: 14.1 MB, less than 97.66% of Python3 online submissions for Merge Intervals.
"""
class Solution:
    def merge_two_intervals(self, interval1: List[int], interval2: List[int]):
        if interval1[0] <= interval2[0] <= interval1[1]:
            return [interval1[0], max(interval1[1], interval2[1])]
        elif interval2[0] <= interval1[0] <= interval2[1]:
            return [interval2[0], max(interval1[1], interval2[1])]
        else:
            return None

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Assume we can modify intervals in-place
        # Sorts lexicographically
        intervals.sort()

        for i in range(len(intervals)-1):
            new_interval = self.merge_two_intervals(intervals[i], intervals[i+1])
            if new_interval is not None:
                intervals[i] = None
                intervals[i+1] = new_interval

        return [interval for interval in intervals if interval is not None]
