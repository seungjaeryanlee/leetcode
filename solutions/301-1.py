"""
OrderedDict solution for Algorithms #301: Remove Invalid Parentheses

- Space Complexity: O(N)
- Time Complexity: O(2^N)

Runtime: 228 ms, faster than 36.57% of Python3 online submissions for Remove Invalid Parentheses.
Memory Usage: 13.5 MB, less than 33.91% of Python3 online submissions for Remove Invalid Parentheses.
"""
from collections import OrderedDict


class Solution:
    def _is_valid(self, candidate: str, extra_left_count: int):
        if not candidate: return False # We will add it manually if needed
        if extra_left_count != 0: return False

        count = 0
        for c in candidate:
            if c == '(': count += 1
            if c == ')': count -= 1
            if count < 0: return False

        return True

    def removeInvalidParentheses(self, s: str) -> List[str]:
        extra_left_count = 0
        for c in s:
            if c == '(': extra_left_count += 1
            if c == ')': extra_left_count -= 1

        # It's a Set (Unique elements) + Queue (FIFO)
        candidate_set = OrderedDict({s: extra_left_count})

        output = []
        while candidate_set:
            # Get oldest candidate
            candidate, extra_left_count = next(iter(candidate_set.items()))
            del candidate_set[candidate]

            # Done if the oldest element is shorter than already found solution
            if output and len(candidate) < len(output[0]): break

            # Check if the candidate is valid
            if self._is_valid(candidate, extra_left_count):
                output.append(candidate)

            # If not, let's delete another parenthesis
            else:
                for i, c in enumerate(candidate):
                    if c == '(':
                        candidate_set[candidate[:i] + candidate[i+1:]] = extra_left_count-1
                    if c == ')':
                        candidate_set[candidate[:i] + candidate[i+1:]] = extra_left_count+1

        # If nothing is found, removing all parentheses is always a valid solution
        # ex) ')(a' -> 'a'
        return output if output else [''.join([c for c in s if c not in '()'])]
