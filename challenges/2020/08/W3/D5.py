"""
Solution for August LeetCoding Challenges Week 3 Day 5: Numbers With Same Consecutive Differences
"""
from collections import deque


class Solution:
    """
    Use BFS to append digits one by one.

    Space : O(2^N)
    ------------
    At any time, the BFS queue only holds sequences that are either length L or L+1 for some L.
    Therefore, it is biggest when L+1 = N, so it holds at most 2^{N-1} + 2^N elements.

    Time : O(N 2^N)
    -----------
    There are 2^N potential sequences of length N, and it takes N time to build each sequence.

    Runtime: 48 ms / 56.74%
    Memory Usage: 14 MB / 60.00%
    """
    def _is_valid(self, num: int) -> bool:
        return 0 <= num and num <= 9

    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1: return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if K == 0:
            return [
                "1" * N,
                "2" * N,
                "3" * N,
                "4" * N,
                "5" * N,
                "6" * N,
                "7" * N,
                "8" * N,
                "9" * N,
            ]

        output = set()
        d = deque([[1], [2], [3], [4], [5], [6], [7], [8], [9]])
        while d:
            if len(d[0]) == N:
                break
            seq = d.popleft()
            if self._is_valid(seq[-1] + K):
                new_seq = seq.copy()
                new_seq.append(seq[-1] + K)
                d.append(new_seq)
            if self._is_valid(seq[-1] - K):
                new_seq = seq.copy()
                new_seq.append(seq[-1] - K)
                d.append(new_seq)

        return ["".join(str(digit) for digit in seq) for seq in d]
