"""
Dynamic programming solution for Algorithms #139 (Word Break).

- N: len(s)
- Space Complexity: O(N)
- Time Complexity: O(N^3)
  - Substring operation: O(N)

Runtime: 32 ms, faster than 99.04% of Python3 online submissions for Word Break.
Memory Usage: 12.9 MB, less than 99.29% of Python3 online submissions for Word Break.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Edge cases
        if not s: return True
        if not wordDict: return False

        # For faster search, use Dict instead of List
        wordDict = {word: None for word in wordDict}

        # If dp[i] == True, s[:dp[i]] can be word-broken
        # NOTE: We want to find dp[len(s)], so the size is len(s) + 1
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
            # NOTE: dp[i] defaults to False

        return dp[len(s)]
