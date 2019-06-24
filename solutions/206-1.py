"""
Iterative solution for Algorithms #206: Reverse Linked List

- Space Complexity: O(1)
- Time Complexity: O(N)

Runtime: 32 ms, faster than 99.09% of Python3 online submissions for Reverse Linked List.
Memory Usage: 14.4 MB, less than 74.88% of Python3 online submissions for Reverse Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Edge cases
        if not head: return None

        previous_node = None
        current_node = head # We can use `head` as is, but just for better name :)
        next_node = current_node.next
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            
        return previous_node
