"""
Runtime: 32 ms, faster than 96.77% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List.
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
