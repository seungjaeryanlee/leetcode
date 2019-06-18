"""
Recursion-based DFS solution for Algorithms #79: Word Search.

Runtime: 152 ms, faster than 93.82% of Python3 online submissions for Word Search.
Memory Usage: 14.3 MB, less than 56.07% of Python3 online submissions for Word Search.
"""
from collections import deque


class Solution:
    def find_word(self, board, i, j, word, visited):
        if not word: return True

        visited[i][j] = True

        is_found = False
        if i-1 >= 0 and not visited[i-1][j] and board[i-1][j] == word[0]:
            is_found |= self.find_word(board, i-1, j, word[1:], visited)
        if not is_found and j-1 >= 0 and not visited[i][j-1] and board[i][j-1] == word[0]:
            is_found |= self.find_word(board, i, j-1, word[1:], visited)
        if not is_found and i+1 <= len(board)-1 and not visited[i+1][j]and board[i+1][j] == word[0]:
            is_found |= self.find_word(board, i+1, j, word[1:], visited)
        if not is_found and j+1 <= len(board[0])-1 and not visited[i][j+1] and board[i][j+1] == word[0]:
            is_found |= self.find_word(board, i, j+1, word[1:], visited)

        visited[i][j] = False

        return is_found

    def exist(self, board: List[List[str]], word: str) -> bool:
        # Edge cases
        if not word: return True
        if not board: return False

        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == word[0]:
                    visited[i][j] = True
                    if self.find_word(board, i, j, word[1:], visited):
                        return True
                    visited[i][j] = False

        return False
