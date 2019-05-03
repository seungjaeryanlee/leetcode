"""
Solution for Algorithms #25: Reverse Nodes in k-Group

Runtime: 56 ms, faster than 78.42% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 14.4 MB, less than 5.33% of Python3 online submissions for Reverse Nodes in k-Group.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 1:
            return head

        # Find length
        length = 0
        current = head
        while current is not None:
            current = current.next
            length += 1

        # NOTE There is a test case contradicting problem description, requiring this if statement
        if length < k:
            return head

        new_head = None # Head of the modified list
        last_group_head = None # Head of the last k-Group
        group_head = head # Head of current k-Group
        for _ in range(int(length / k)):
            node = group_head
            next_node = node.next

            for _ in range(k - 1):
                # Reverse "next" reference of next_node
                next_next_node = next_node.next
                next_node.next = node
                # Move to next pair
                node = next_node
                next_node = next_next_node

            if last_group_head is not None:
                last_group_head.next = node
            else:
                new_head = node
            last_group_head = group_head
            group_head = next_node

        if last_group_head is not None:
            last_group_head.next = next_node

        return new_head
