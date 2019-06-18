"""
Non-string-sorting solution for Algorithms #49: Group Anagrams.

- N: Number of strings
- K: Maximum length of strings
- Space Complexity: O(NK)
- Time Complexity: O(NK)
  - Generate key: O(K)

Runtime: 128 ms, faster than 41.78% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.7 MB, less than 17.10% of Python3 online submissions for Group Anagrams.
"""
class Solution:
    def _get_key_from_str(self, s):
        # NOTE Probably could use Python Counter
        letter_counts = [0] * 26
        for c in s:
            letter_counts[ord(c) - ord('a')] += 1

        # return '.'.join([str(n) for n in letter_counts])
        return tuple(letter_counts)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Edge cases (len == 0 or 1)
        if not strs: return []
        if len(strs) == 1: return [[strs[0]]]

        anagram_groups = {}
        for s in strs:
            key = self._get_key_from_str(s)
            if key in anagram_groups:
                anagram_groups[key].append(s)
            else:
                anagram_groups[key] = [s]

        return [v for _, v in anagram_groups.items()]
