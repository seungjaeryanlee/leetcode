"""
Solution for July LeetCoding Challenges Week 1 Day 7: Island Perimeters
"""
from collections import deque


class Solution1:
    """
    Go through each grid element and check neighbors. Optimizes space.

    - Grid size: N
    - Space Complexity: O(1)
    - Time Complexity: O(N)

    Runtime: 752 ms / 26.18%
    Memory Usage: 13.9 MB / 84.17%
    """
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    perimeter += (
                        (1 - grid[i-1][j] if i > 0 else 1)
                        + (1- grid[i+1][j] if i < len(grid) - 1 else 1)
                        + (1 - grid[i][j-1] if j > 0 else 1)
                        + (1 - grid[i][j+1] if j < len(grid[0]) - 1 else 1)
                    )

        return perimeter


class Solution2:
    """
    Only go through the island with DFS and check neighbors.

    - Grid size: N
    - Space Complexity: O(N)
    - Time Complexity: O(N)

    Runtime: 840 ms / 16.32%
    Memory Usage: 14.1 MB / 39.68%
    """
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Find a land
        d = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    d.append((i, j))
                    break
            if len(d):
                break
        # BFS with queue
        perimeter = 0
        added = [[False] * len(grid[0]) for _ in range(len(grid))]
        added[i][j] = True
        while d:
            i, j = d.popleft()
            if i > 0 and grid[i-1][j]:
                if not added[i-1][j]:
                    d.append((i-1, j))
                    added[i-1][j] = True
            else:
                perimeter += 1
                
            if i < len(grid) - 1 and grid[i+1][j]:
                if not added[i+1][j]:
                    d.append((i+1, j))
                    added[i+1][j] = True
            else:
                perimeter += 1
                
            if j > 0 and grid[i][j-1]:
                if not added[i][j-1]:
                    d.append((i, j-1))
                    added[i][j-1] = True
            else:
                perimeter += 1
                
            if j < len(grid[0]) - 1 and grid[i][j+1]:
                if not added[i][j+1]:
                    d.append((i, j+1))
                    added[i][j+1] = True
            else:
                perimeter += 1
        
        return perimeter
