"""
Recursive solution for Algorithms #206: Reverse Linked List

- Space Complexity: O(N)
  - From recursion stack space
- Time Complexity: O(N)

Runtime: 40 ms, faster than 85.51% of Python3 online submissions for Reverse Linked List.
Memory Usage: 23.8 MB, less than 5.03% of Python3 online submissions for Reverse Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseListRecursion(self, head: ListNode) -> ListNode:
        if head.next is None: return head

        # Receive the new head after reversing linked list
        new_head = self.reverseList(head.next)
        # Reverse direction of head.next
        head.next.next = head

        return new_head

    def reverseList(self, head: ListNode) -> ListNode:
        # Edge cases
        if not head: return None

        new_head = self.reverseListRecursion(head)
        head.next = None

        return new_head
