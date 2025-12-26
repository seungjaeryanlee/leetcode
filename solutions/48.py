class Solution:
    def rotate_coord(self, size, y, x) -> tuple[int, int]:
        mid = (size - 1) / 2
        dist_y, dist_x = mid - y, mid - x

        new_y = int(mid - dist_x)
        new_x = int(mid + dist_y)
        print(f"Size: {size} | Mid: {mid} | Coord: ({y}, {x}) | Rotated: ({new_y}, {new_x})")
        return new_y, new_x 

    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix

        size = len(matrix)

        # NOTE: We only add +1 for one side so that the middle row/column of odd-size square is not rotated twice
        for y in range((size+1) // 2):
            for x in range(size // 2):
                temp = matrix[y][x]
                new_y, new_x = y, x
                for i in range(4):
                    new_y, new_x = self.rotate_coord(size, new_y, new_x)
                    matrix[new_y][new_x], temp = temp, matrix[new_y][new_x]
