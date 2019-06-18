"""
Dictionary-based solution for Algorithms #49: Group Anagrams.

- N: Number of strings
- K: Maximum length of strings
- Space Complexity: O(NK)
- Time Complexity: O(NK log K)
  - Sort each string: O(K log K)

Runtime: 112 ms, faster than 91.61% of Python3 online submissions for Group Anagrams.
Memory Usage: 15.9 MB, less than 73.23% of Python3 online submissions for Group Anagrams.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Edge cases (len == 0 or 1)
        if not strs: return []
        if len(strs) == 1: return [[strs[0]]]

        anagram_groups = {}
        for s in strs:
            key = ''.join(sorted(list(s)))
            if key in anagram_groups:
                anagram_groups[key].append(s)
            else:
                anagram_groups[key] = [s]

        return [v for _, v in anagram_groups.items()]
