"""
Space-efficient solution for Algorithms #289: Game of Life

- M: Number of Rows
- N: Number of columns
- Space Complexity: O(1)
- Time Complexity: O(MN)

Runtime: 32 ms, faster than 97.22% of Python3 online submissions for Game of Life.
Memory Usage: 13.2 MB, less than 43.47% of Python3 online submissions for Game of Life.
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Edge cases
        if not board or not board[0]: return

        # -1 : Was Dead, now Alive
        #  0 : Was Dead
        #  1 : Was Alive
        #  2 : Was Alive, now Dead
        # These numbers are chosen so a simple > 0 can check past life
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                alive_neighbors_count = 0
                alive_neighbors_count += int(i-1 >= 0 and board[i-1][j] > 0)
                alive_neighbors_count += int(i-1 >= 0 and j-1 >= 0 and board[i-1][j-1] > 0)
                alive_neighbors_count += int(i-1 >= 0 and j+1 < len(row) and board[i-1][j+1] > 0)
                alive_neighbors_count += int(j-1 >= 0 and board[i][j-1] > 0)
                alive_neighbors_count += int(j+1 < len(row) and board[i][j+1] > 0)
                alive_neighbors_count += int(i+1 < len(board) and board[i+1][j] > 0)
                alive_neighbors_count += int(i+1 < len(board) and j-1 >= 0 and board[i+1][j-1] > 0)
                alive_neighbors_count += int(i+1 < len(board) and j+1 < len(row) and board[i+1][j+1] > 0)

                # Alive -> Dead
                if cell and not (2 <= alive_neighbors_count <= 3): 
                    board[i][j] = 2
                # Dead -> Alive
                elif not cell and alive_neighbors_count == 3:
                    board[i][j] = -1

        # Remove nonstandard notation
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == -1: board[i][j] = 1
                if cell == 2: board[i][j] = 0
