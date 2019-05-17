"""
Solution for Algorithms #39: Combination Sum

Runtime: 68 ms, faster than 79.90% of Python3 online submissions for Combination Sum.
Memory Usage: 13.2 MB, less than 45.04% of Python3 online submissions for Combination Sum.
"""
from copy import deepcopy


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        next_candidates = {}
        for i in range(len(candidates)-1):
            next_candidates[candidates[i]] = candidates[i+1]
        next_candidates[candidates[-1]] = None

        solutions = []
        solution_queue = []
        # Populate initial solution candidate
        while sum(solution_queue) < target:
            solution_queue.append(candidates[0])

        while solution_queue:
            if sum(solution_queue) == target:
                solutions.append(deepcopy(solution_queue))

            # Find next solution candidate
            del solution_queue[-1]
            while solution_queue:
                solution_queue[-1] = next_candidates[solution_queue[-1]]
                if solution_queue[-1] is None:
                    del solution_queue[-1]
                else:
                    break
            while solution_queue and sum(solution_queue) < target:
                solution_queue.append(solution_queue[-1])

        return solutions
