"""
Solution for Algorithms #22: Generate Parentheses

Runtime: 40 ms, faster than 85.82% of Python3 online submissions for Generate Parentheses.
Memory Usage: 13.3 MB, less than 5.10% of Python3 online submissions for Generate Parentheses.
"""
class Solution:
    def recursion(self, prefix: str, left: int, right: int):
        if left == 0:
            return [prefix + ')' * right]

        solutions = []
        if left > 0:
            solutions += self.recursion(prefix+'(', left-1, right)
        if left < right:
            solutions += self.recursion(prefix+')', left, right-1)

        return solutions

    def generateParenthesis(self, n: int) -> List[str]:
        return self.recursion('', n, n)
