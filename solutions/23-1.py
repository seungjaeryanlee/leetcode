"""
Solution for Algorithms #23: Merge k Sorted Lists

Keep sorted list of heads. O(kN)

Runtime: 108 ms, faster than 43.10% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 16.5 MB, less than 35.22% of Python3 online submissions for Merge k Sorted Lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def insert_to_sorted(self, sorted_nodes, new_node):
        for i, n in enumerate(sorted_nodes):
            if new_node.val <= n.val:
                sorted_nodes.insert(i, new_node)
                return
        sorted_nodes.append(new_node)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy_head = ListNode(0)
        current_head = dummy_head

        # Remove empty ListNodes
        heads = [l for l in lists if l]
        heads.sort(key=lambda h: h.val) # O(k log k)

        while heads: # O(N)
            current_head.next = heads[0]
            current_head = current_head.next

            if heads[0].next is not None:
                new_node = heads[0].next
                del heads[0]
                self.insert_to_sorted(heads, new_node) # O(k)
            else:
                del heads[0]
                # No need to sort since it is already fully sorted

        return dummy_head.next
