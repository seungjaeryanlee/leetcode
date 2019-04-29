"""
Solution for Algorithms #23: Merge k Sorted Lists

Use heapq with modified ListNode class. O(N log k)
TODO I should have used PriorityQueue.

Runtime: 104 ms, faster than 44.90% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 16.3 MB, less than 39.21% of Python3 online submissions for Merge k Sorted Lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


class Solution:
    # Heapq takes no keyword argument, so we make them sortable this way
    def __lt__(self, other):
        return self.val < other.val
    def __gt__(self, other):
        return self.val > other.val

    ListNode.__lt__ = __lt__
    ListNode.__gt__ = __gt__

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy_head = ListNode(0)
        current_head = dummy_head

        # Remove empty ListNodes
        heads = [l for l in lists if l]
        heapq.heapify(heads) # O(k)
        while heads: # O(N)
            # TODO Faster with heappushpop?
            min_head = heapq.heappop(heads) # O(log k)
            current_head.next = min_head
            current_head = current_head.next

            if min_head.next is not None:
                heapq.heappush(heads, min_head.next) # O(log k)

        return dummy_head.next
