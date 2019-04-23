"""
Solution for Algorithms #13: Roman to Integer

Runtime: 80 ms, faster than 77.78% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.3 MB, less than 5.05% of Python3 online submissions for Roman to Integer.
"""
import copy


# Uses more space, but more extendable and cleaner
symlist = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
sym_to_val = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        # Don't change the given string
        s = copy.copy(s)
        answer = 0

        while s:
            for sym in symlist:
                if len(s) > 1 and s[0] != sym and s[1] == sym:
                    answer += sym_to_val[s[1]] - sym_to_val[s[0]]
                    s = s[2:]
                    break
                if s[0] == sym:
                    answer += sym_to_val[s[0]]
                    s = s[1:]
                    break

        return answer
