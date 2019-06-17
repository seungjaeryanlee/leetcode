"""
Solution for Algorithms #253: Meeting Rooms II

- N: Number of intervals
- Space Complexity: O(N)
  - The `timestamps` list.
- Time Complexity: O(N log N)
  - Sorting `timestamps` take O(N log N).

Runtime: 48 ms, faster than 76.49% of Python3 online submissions for Meeting Rooms II.
Memory Usage: 16.5 MB, less than 74.42% of Python3 online submissions for Meeting Rooms II.
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0

        # Note that the words matter: lexicographically 'start' > 'end'
        # If there is (1, 'end') and (1, 'start'), end comes first
        # So [[0, 1], [1, 2]] returns 1, not 2
        timestamps = (
              [(interval[0], 'start') for interval in intervals]
            + [(interval[1], 'end') for interval in intervals]
        )
        timestamps.sort()

        max_count = 0
        count = 0
        for t in timestamps:
            if t[1] == 'start':
                count += 1
                if count > max_count:
                    max_count = count
            else: # t[1] == 'end'
                count -= 1

        return max_count
