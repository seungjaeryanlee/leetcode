"""
Solution for Algorithms #10: Regular Expression Matching.

Runtime: 1148 ms, faster than 30.27% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 13.2 MB, less than 5.32% of Python3 online submissions for Regular Expression Matching.
"""
def isMatchRecursion(s, p):
    # print('Called with s: {} and p: {}'.format(s, p))
    # Terminal condition
    if not s and not p:
        return True

    # Star token
    if len(p) > 1 and p[1] == '*':
        # Star could mean 0
        if isMatchRecursion(s[:], p[2:]):
            return True
        # Star could mean 1 or more
        for i, c in enumerate(s):
            if p[0] == '.' or p[0] == c:
                if isMatchRecursion(s[i+1:], p[2:]):
                    return True
            # Found character not covered by *
            else:
                break

    # No star token
    else:
        if not s or not p:
            return False

        if p[0] == '.' or p[0] == s[0]:
            if isMatchRecursion(s[1:], p[1:]):
                return True

    return False


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return isMatchRecursion(s, p)
