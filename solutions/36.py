"""
Solution for Algorithms #36: Valid Sudoku

Runtime: 52 ms, faster than 85.00% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.1 MB, less than 5.10% of Python3 online submissions for Valid Sudoku.
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check Rows
        for row in board:
            flags = [False] * 10

            for cell in row:
                if cell == ".": continue
                if flags[int(cell)]:
                    return False
                else:
                    flags[int(cell)] = True

        # Check Columns
        for column_i in range(9):
            flags = [False] * 10

            for row_i in range(9):
                if board[row_i][column_i] == ".": continue
                if flags[int(board[row_i][column_i])]:
                    return False
                else:
                    flags[int(board[row_i][column_i])] = True

        # Check Sub-boxes
        for subbox_row_i in range(3):
            for subbox_column_i in range(3):
                flags = [False] * 10

                for row_i in range(subbox_row_i * 3, subbox_row_i * 3 + 3):
                    for column_i in range(subbox_column_i * 3, subbox_column_i * 3 + 3):
                        if board[row_i][column_i] == ".": continue
                        if flags[int(board[row_i][column_i])]:
                            return False
                        else:
                            flags[int(board[row_i][column_i])] = True

        return True
