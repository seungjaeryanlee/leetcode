"""
List-of-list-based solution for Algorithms #49: Group Anagrams.

- N: Number of strings
- K: Maximum length of strings
- Space Complexity: O(NK)
- Time Complexity: O(N log N + NK log K)
  - Sort each string: O(K log K)
  - Sort `strs`: O(N log N)
  - Run through `strs` once: O(N)

Runtime: 116 ms, faster than 77.62% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.7 MB, less than 17.79% of Python3 online submissions for Group Anagrams.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Edge cases (len == 0 or 1)
        if not strs: return []
        if len(strs) == 1: return [[strs[0]]]

        strs = [(sorted(list(s)), s) for s in strs]
        strs.sort()

        anagram_groups = []
        anagram_group = [strs[0][1]]
        for i in range(1, len(strs)):
            if strs[i-1][0] == strs[i][0]:
                anagram_group.append(strs[i][1])
            else:
                anagram_groups.append(anagram_group)
                anagram_group = [strs[i][1]]

        # Add last group
        if anagram_group:
            anagram_groups.append(anagram_group)

        return anagram_groups
