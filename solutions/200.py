"""
Solution for Algorithms #200: Number of Islands

Runtime: 96 ms, faster than 36.87% of Python3 online submissions for Number of Islands.
Memory Usage: 13.7 MB, less than 94.63% of Python3 online submissions for Number of Islands.
"""
import copy
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        # If we can't modify `grid` directly
        # checked = copy.deepcopy(grid)
        # If we can modify `grid` directly
        checked = grid

        island_count = 0
        height = len(checked)
        width = len(checked[0])
        for i in range(height):
            for j in range(width):
                if checked[i][j] == '1':
                    island_count += 1
                    q = deque([(i, j)])
                    while q:
                        element = q.popleft()
                        if checked[element[0]][element[1]] == '1': # Still land
                            checked[element[0]][element[1]] = '0'
                            if element[0]+1 < height and (element[0]+1, element[1]) not in q:
                                q.append((element[0]+1, element[1]))
                            if element[0]-1 >= 0 and (element[0]-1, element[1]) not in q:
                                q.append((element[0]-1, element[1]))
                            if element[1]+1 < width and (element[0], element[1]+1) not in q:
                                q.append((element[0], element[1]+1))
                            if element[1]-1 >= 0 and (element[0], element[1]-1) not in q:
                                q.append((element[0], element[1]-1))

        return island_count
