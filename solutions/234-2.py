"""
O(1) space Solution for Algorithms #234: Palindrome Linked List

- Space Complexity: O(1)
- Time Complexity: O(N)

Runtime: 80 ms, faster than 70.61% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 23.6 MB, less than 94.65% of Python3 online submissions for Palindrome Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def _reverse_list(self, old_head: ListNode) -> ListNode:
        previous_node = None
        while old_head is not None:
            next_node = old_head.next
            old_head.next = previous_node
            previous_node = old_head
            old_head = next_node

        return previous_node

    def isPalindrome(self, head: ListNode) -> bool:
        # Edge cases
        if head is None: return True

        # Compute length of list
        length = 0
        current = head
        while current is not None:
            current = current.next
            length += 1

        # Find start of second half
        current = head
        for _ in range(length // 2):
            current = current.next
        if length % 2:
            current = current.next

        # Flip second half of list
        second_head = self._reverse_list(current)

        # Compare first half and second half iteratively
        for _ in range(length // 2):
            if head.val != second_head.val:
                return False
            head = head.next
            second_head = second_head.next

        return True
