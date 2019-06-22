"""
Naive solution for Algorithms #289: Game of Life

- M: Number of Rows
- N: Number of columns
- Space Complexity: O(MN)
- Time Complexity: O(MN)

Runtime: 32 ms, faster than 97.22% of Python3 online submissions for Game of Life.
Memory Usage: 13.3 MB, less than 24.45% of Python3 online submissions for Game of Life.
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Edge cases
        if not board or not board[0]: return

        alive_neighbors_counts = [[0] * len(board[0]) for _ in range(len(board))]
        # Count alive neighbors
        # For every alive cell, increment neighbor's count by 1
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if not cell: continue

                if i-1 >= 0:
                    alive_neighbors_counts[i-1][j] += 1
                    if j-1 >= 0:
                        alive_neighbors_counts[i-1][j-1] += 1
                    if j+1 < len(row):
                        alive_neighbors_counts[i-1][j+1] += 1
                if i+1 < len(board):
                    alive_neighbors_counts[i+1][j] += 1
                    if j-1 >= 0:
                        alive_neighbors_counts[i+1][j-1] += 1
                    if j+1 < len(row):
                        alive_neighbors_counts[i+1][j+1] += 1
                if j-1 >= 0:
                    alive_neighbors_counts[i][j-1] += 1
                if j+1 < len(row):
                    alive_neighbors_counts[i][j+1] += 1

        # Update board
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell:
                    board[i][j] = int(2 <= alive_neighbors_counts[i][j] <= 3)
                else:
                    board[i][j] = int(alive_neighbors_counts[i][j] == 3)
