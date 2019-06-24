"""
Set + Filter solution for Algorithms #301: Remove Invalid Parentheses

- Space Complexity: O(N)
- Time Complexity: O(2^N)

Runtime: 284 ms, faster than 26.67% of Python3 online submissions for Remove Invalid Parentheses.
Memory Usage: 14 MB, less than 13.95% of Python3 online submissions for Remove Invalid Parentheses.
"""
class Solution:
    def _is_valid(self, candidate):
        if not candidate: return False # We will add it manually if needed

        count = 0
        for c in candidate:
            if c == '(': count += 1
            if c == ')': count -= 1
            if count < 0: return False

        return count == 0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        # It's a Set (Unique elements) + Queue (FIFO)
        candidate_set = {s}

        output = []
        while candidate_set:
            # Check if the candidate_set has any valid candidates
            valid_candidates = list(filter(self._is_valid, candidate_set))
            
            if valid_candidates:
                return valid_candidates
            else:
                candidate_set = {candidate[:i] + candidate[i+1:] for candidate in candidate_set for i in range(len(candidate))}

        # If nothing is found, removing all parentheses is always a valid solution
        # ex) ')(a' -> 'a'
        return output if output else [''.join([c for c in s if c not in '()'])]
