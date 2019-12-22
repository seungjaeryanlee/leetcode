"""
Solution for Algorithms #953: Verifying an Alien Dictionary

- N: Number of words
- M: Length of words
- Space Complexity: O(1)
- Time Complexity: O(MN)

Runtime: 24 ms, faster than 99.48% of Python3 online submissions for Verifying an Alien Dictionary.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Verifying an Alien Dictionary.
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Empty or 1-element is sorted
        if len(words) < 2:
            return True

        for i in range(len(words)-1):
            sorted = False
            for j in range(min(len(words[i]), len(words[i+1]))):
                if order.index(words[i][j]) > order.index(words[i+1][j]):
                    return False
                elif order.index(words[i][j]) < order.index(words[i+1][j]):
                    sorted = True
                    break

            if not sorted and len(words[i]) > len(words[i+1]):
                return False

        return True
