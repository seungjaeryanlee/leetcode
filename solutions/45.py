from collections import deque


class Solution1:
    """
    Go over each step.
    """
    def jump(self, nums: list[int]) -> int:
        min_jumps = [None] * len(nums)
        min_jumps[0] = 0
        for i, num in enumerate(nums):
            for j in range(1, num+1):
                if i+j >= len(nums):
                    break
                if min_jumps[i+j] is None:
                    min_jumps[i+j] = min_jumps[i] + 1
                else:
                    min_jumps[i+j] = min(min_jumps[i+j], min_jumps[i] + 1)

        return min_jumps[-1]


class Solution2:
    """
    BFS-style approach.
    """
    def jump(self, nums: list[int]) -> int:
        d = deque([(0, 0)])
        visited = [False] * len(nums)

        while d:
            i, min_jump = d.popleft()
            if visited[i]:
                continue
            visited[i] = True

            if i == len(nums) - 1:
                return min_jump
            if i + nums[i] >= len(nums) - 1:
                return min_jump + 1

            for j in range(nums[i], 0, -1):
                if i+j >= len(nums):
                    continue
                d.append((i+j, min_jump+1))

class Solution3:
    """
    Use range
    """
    def jump(self, nums: list[int]) -> int:
        reachable_range = (0, 0)
        jumps = 0
        while not (reachable_range[0] <= len(nums) - 1 <= reachable_range[1]):
            new_max = reachable_range[0] + 1
            for i in range(reachable_range[0], reachable_range[1] + 1):
                new_max = max(new_max, i + nums[i])
        
            reachable_range = (reachable_range[1]+1, new_max)
            jumps += 1

        return jumps