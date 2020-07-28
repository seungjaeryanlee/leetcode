"""
Solution for July LeetCoding Challenges Week 4 Day 7: Task Scheduler
"""
class Solution:
    """
    Find the tasks that occur maximum amount of times. Then, observe that these
    tasks must be separated by n (the cooldown period). During the cooldown
    period, we can either be idle or perform other unallocated tasks that did
    not occur maximum amount of times. If the number of unallocated tasks is
    less or equal to the cooldown slots, then we can simply ignore the other
    tasks and calculate the minimum time using the most frequent tasks and the
    cooldown period. If there are more unallocated tasks than the slots, we
    simply append them at the end.

    Note that this solution requires proof that the we can allocate the
    unallocated tasks without violating the cooldown period. I have not proved
    this.

    Space : O(1)
    ------------
    Nothing taking up space other than a few variables.

    Time : O(1)
    -----------
    Nothing taking up time: this is a mathematical solution.

    Runtime: 24 ms / 97.30%
    Memory Usage: 13.5 MB / 99.60%
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)

        task_counts = Counter(tasks)
        max_count = max(task_counts.values())
        max_tasks = [task for task, count in task_counts.items() if count == max_count]
        slots = (max_count - 1) * (n + 1 - len(max_tasks))
        unallocated_tasks = len(tasks) - len(max_tasks) * max_count
        print(f"slots: {slots}")
        print(f"unallocated_tasks: {unallocated_tasks}")

        if unallocated_tasks <= slots:
            return (max_count - 1) * (n + 1) + len(max_tasks)
        else:
            return len(tasks)
