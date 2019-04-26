"""
Solution for Algorithms #21: Merge Two Sorted Lists

Runtime: 44 ms, faster than 88.71% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.2 MB, less than 5.06% of Python3 online submissions for Merge Two Sorted Lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0) # This is dummy node
        last = head
        while l1 is not None and l2 is not None:
            # print('L1 {} L2 {}'.format(l1.val, l2.val))
            if l1.val < l2.val:
                last.next = l1
                last = last.next
                l1 = l1.next
            else:
                last.next = l2
                last = last.next
                l2 = l2.next

        if l1 is not None:
            last.next = l1
        elif l2 is not None:
            last.next = l2

        return head.next
