"""
Solution for Algorithms #17: Letter Combinations of a Phone Number

TODO Is this substantially inefficient compared to backtracking? Let's check backtracking later.

Runtime: 36 ms, faster than 80.76% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13 MB, less than 5.86% of Python3 online submissions for Letter Combinations of a Phone Number.
"""
digit_to_letters = [
    '',
    '',
    'abc',
    'def',
    'ghi',
    'jkl',
    'mno',
    'pqrs',
    'tuv',
    'wxyz',
]


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        prefixes = list(digit_to_letters[int(digits[0])])
        for digit in digits[1:]:
            new_prefixes = []
            for letter in digit_to_letters[int(digit)]:
                new_prefixes.extend([prefix + letter for prefix in prefixes])

            prefixes = new_prefixes

        return prefixes
