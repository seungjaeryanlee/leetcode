import copy


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return copy.copy(s)

        rows = [''] * numRows

        current_row = 0
        move_forward = True

        for c in s:
            rows[current_row] += c

            current_row += 1 if move_forward else -1
            # Change direction
            if current_row == 0:
                move_forward = True
            if current_row == numRows -1:
                move_forward = False

        return ''.join(rows)
