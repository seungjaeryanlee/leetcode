"""
Solution for Algorithms #19: Remove Nth Node From End of List

Double-pass.

Runtime: 40 ms, faster than 92.06% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.2 MB, less than 5.60% of Python3 online submissions for Remove Nth Node From End of List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Method 1: 1st pass to find length, 2nd pass to remove node
        current = head
        length = 1
        while current.next is not None:
            current = current.next
            length += 1
        print(length)

        # Edge case: Remove first element (length == n)
        if length == n:
            return head.next

        before_nth = head  # The node before the node to remove
        for _ in range(length - n - 1):
            before_nth = before_nth.next
        before_nth.next = before_nth.next.next

        return head
