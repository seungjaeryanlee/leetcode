"""
Solution for Algorithms #394: Decode String

- N: Length of `str`
- Space Complexity: O(N)
- Time Complexity: ?

Runtime: 36 ms, faster than 75.08% of Python3 online submissions for Decode String.
Memory Usage: 13.1 MB, less than 85.73% of Python3 online submissions for Decode String.
"""
from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        # Edge case
        if not s: return ''

        d = deque([])
        phrase = ''
        repeat = ''
        for i, c in enumerate(s):
            if c in '0123456789':
                if phrase:
                    d.append(phrase)
                    phrase = ''
                d.append(c)

            elif c == '[':
                # Would be preceded by number, so phrase is empty
                d.append('[')

            elif c == ']':
                # Get phrase between '[' and ']'
                while d[-1] is not '[':
                    c = d.pop()
                    phrase = c + phrase
                d.pop() # Remove '['
                
                # Get number before '['
                repeat = ''
                while d and d[-1] in '0123456789':
                    repeat = d.pop() + repeat

                # Add repeated phrase
                d.append(''.join([phrase for _ in range(int(repeat))]))
                phrase = ''

            else:
                phrase += c

        # Add any leftover phrase
        d.append(phrase)

        return ''.join(d)
