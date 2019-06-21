"""
Solution for Algorithms #621 (Task Scheduler).

- N: Length of `tasks` (not n)
- Space Complexity: O(N)
  - `tasks_count` is the only O(N)
- Time Complexity: O(N)

Runtime: 64 ms, faster than 78.38% of Python3 online submissions for Task Scheduler.
Memory Usage: 13.3 MB, less than 39.93% of Python3 online submissions for Task Scheduler.
"""
from collections import defaultdict


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count each task
        tasks_count = defaultdict(int)
        for task in tasks:
            tasks_count[task] += 1
        max_count = 0 # Number of most frequent tasks
        max_task_count = 0 # Number of tasks with maximum
        for i in range(26):
            if max_count < tasks_count[chr(ord('A') + i)]:
                max_count = tasks_count[chr(ord('A') + i)]
                max_task_count = 1
            elif max_count == tasks_count[chr(ord('A') + i)]:
                max_task_count += 1

        # Suppose there are "max_task_count" most frequent tasks (appear "max_count" times)
        # Denote them (M1), (M2), (M3), ... , (Mx)
        # Then these must be scheduled (M1)(M2)(M3)...(Mx)(idle)...(idle)(M1)(M2)(M3)...(Mx)(idle)...
        # There must be at least "n" tasks between (Mi)
        # Thus, each (M1)...(Mx)(idle)...(idle) is at least "n+1" long
        # So to have these tasks "max_count" times, we need "max_count-1" of these blocks
        # Now, other tasks can always be crammed into the remaining spots
        if (n + 1) * (max_count - 1) + max_task_count < len(tasks):
            return len(tasks)
        return (n + 1) * (max_count - 1) + max_task_count
