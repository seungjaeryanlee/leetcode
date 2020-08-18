"""
Solution for August LeetCoding Challenges Week 2 Day 7: Longest Palindrome
"""
from collections import deque


class Solution:
    """
    Count characters and add all pairs and add one more for the middle of the palindrome if there
    is a character with an odd count.

    Space : O(K)
    ------------
    K is the number of unique characters in the string. We need to save the counter per character,
    so O(K) space is needed.

    Time : O(K)
    -----------
    N is the length of the input string. To count the characters in the string, we need to loop
    through the string once, which takes O(N) time.

    Runtime: 24 ms / 95.69%
    Memory Usage: 13.9 MB / 25.13%
    """
        frequencies = Counter(s)

        longest_length = 0
        for char, freq in frequencies.items():
            longest_length += freq // 2 * 2
            if longest_length % 2 == 0 and freq % 2 == 1:
                longest_length += 1

        return longest_length
