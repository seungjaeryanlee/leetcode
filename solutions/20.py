"""
Solution for Algorithms #20: Valid Parentheses

Runtime: 36 ms, faster than 87.97% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.2 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        paren_stack = []
        for c in s:
            if c in ['(', '{', '[']:
                paren_stack.append(c)
            elif c == ')':
                if not paren_stack or paren_stack[-1] != '(': return False
                else: del paren_stack[-1]
            elif c == '}':
                if not paren_stack or paren_stack[-1] != '{': return False
                else: del paren_stack[-1]
            elif c == ']':
                if not paren_stack or paren_stack[-1] != '[': return False
                else: del paren_stack[-1]

        return (not paren_stack)
