"""
Solution for Algorithms #234: Palindrome Linked List

- Space Complexity: O(N)
- Time Complexity: O(N)
"""
from collections import deque


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Edge cases
        if head is None: return True

        length = 0
        current = head
        while current is not None:
            current = current.next
            length += 1

        d = deque([])
        current = head
        # Add first half to deque (used as Stack)
        for i in range(length // 2):
            d.append(current.val)
            current = current.next
        if length % 2:
            current = current.next

        # Check second half to deque
        while current is not None:
            if current.val != d.pop():
                return False
            current = current.next

        return True
