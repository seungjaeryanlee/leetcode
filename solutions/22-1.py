"""
Solution for Algorithms #22: Generate Parentheses

Runtime: 52 ms, faster than 26.31% of Python3 online submissions for Generate Parentheses.
Memory Usage: 13.4 MB, less than 5.10% of Python3 online submissions for Generate Parentheses.
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        combos = self.generateParenthesis(n-1)

        solutions = set()
        for combo in combos:
            spaces = (n-1) * 2
            left_i = 0

            ## 1. Simple method: try every pair
            # for left_i in range(spaces+1):
            #     for right_i in range(left_i, spaces+1):
            #         solutions.append(combo[:left_i] + "(" + combo[left_i:right_i] + ")" + combo[right_i:])

            ## 2. Skip pairs that will generate same result
            while left_i <= spaces:
                right_i = left_i
                while right_i <= spaces:
                    solutions.add(combo[:left_i] + "(" + combo[left_i:right_i] + ")" + combo[right_i:])
                    right_i += 1
                    while right_i <= spaces and combo[right_i-1] == ")":
                        right_i += 1

                left_i += 1
                while left_i <= spaces and combo[left_i-1] == "(":
                    left_i += 1

        return list(solutions)
