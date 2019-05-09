"""
Solution for Algorithms #32: Longest Valid Parentheses

Inefficient solution.

Runtime: 292 ms, faster than 5.04% of Python3 online submissions for Longest Valid Parentheses.
Memory Usage: 13.3 MB, less than 5.85% of Python3 online submissions for Longest Valid Parentheses.
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Convert '()' to '11'
        # The parentheses pairs can have '1's in  between
        s = list(s)
        last_open_c_index = -1
        i = 0
        while i < len(s):
            if s[i] == '(':
                last_open_c_index = i
            if s[i] == ')' and last_open_c_index >= 0:
                s[last_open_c_index] = 1
                s[i] = 1
                if last_open_c_index > 0:
                    i = last_open_c_index - 1 # -1 for the char before
                    while i >= 0 and s[i] == 1:
                        i -= 1
                    i -= 1 # since it will be incremented
                last_open_c_index = -1

            i += 1

        # Counter consecutive '1's
        max_length = 0
        counter = 0
        for c in s:
            if c == '(' or c == ')':
                max_length = max(max_length, counter)
                counter = 0
            else:
                counter += c
        max_length = max(max_length, counter)

        return max_length
