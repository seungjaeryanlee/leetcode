"""
Solution for Algorithms #19: Remove Nth Node From End of List

Single-pass, but more memory.

Runtime: 40 ms, faster than 92.06% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.3 MB, less than 5.60% of Python3 online submissions for Remove Nth Node From End of List.
"""
from collections import deque


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Method 2: Keep deque of size N+1.
        d = deque(maxlen=n+1)

        # Pass through elements, saving N+1 most recent nodes
        current = head
        d.append(head)
        length = 1
        while current.next is not None:
            current = current.next
            d.append(current)
            length += 1

        # Edge case: Removing first element
        if length == n:
            return head.next

        before_nth = d[0]
        before_nth.next = before_nth.next.next

        return head
