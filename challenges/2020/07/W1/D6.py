"""
Solution for July LeetCoding Challenges Week 1 Day 6: Plus One
"""
class Solution1:
    """
    Use carry boolean to check if one is carried over

    - Number of digits: M, N
    - Space Complexity: O(1)
    - Time Complexity: O(max(M, N))

    Runtime: 56 ms / 7.05%
    Memory Usage: 13.7 MB / 78.16%
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                carry = True
                digits[i] = 0
            else:
                carry = False
                digits[i] += 1
                break
        if carry:
            return [1] + digits
        else:
            return digits


class Solution2:
    """
    Infer carried one without an explicit boolean.

    - Number of digits: M, N
    - Space Complexity: O(1)
    - Time Complexity: O(max(M, N))

    Runtime: 52 ms / 10.12%
    Memory Usage: 13.8 MB / 52.25%
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1 and digits[0] == 0:
            return [1]

        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break

        if digits[0] == 0:
            return [1] + digits
        else:
            return digits
