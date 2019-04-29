"""
Solution for Algorithms #24: Swap Nodes in Pairs

Runtime: 60 ms, faster than 14.39% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.2 MB, less than 5.04% of Python3 online submissions for Swap Nodes in Pairs.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        front = head
        head = head.next # Assumes there is a pair
        while front is not None and front.next is not None:
            back = front
            front = back.next
            # There is a pair after this pair
            if front.next is not None and front.next.next is not None:
                back.next = front.next.next
            else:
                back.next = front.next

            # Move to next pair
            new_front = front.next
            front.next = back
            front = new_front

        return head
