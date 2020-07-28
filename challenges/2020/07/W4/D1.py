"""
Solution for July LeetCoding Challenges Week 4 Day 1: Binary Tree Zigzag Level Order Traversal
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Use DFS to get nodes per level, then reverse lists with odd index.

    Space : O(log N)
    ----------------
    d : O(log N)
        Since we use DFS, the deque only carries nodes from at most two levels.
        The number of nodes per level is O(log N).

    Time : O(N)
    -----------
    DFS : O(N)
        All nodes must be visited, which is O(N).
    Zigzag : O((log N)^2)
        There are O(log N) lists, and half of them need to be reversed. For each
        list of length K, O(K) time is needed for list reversal. The biggest list
        has O(log N) nodes, so O((log N)^2).

    Runtime: 28 ms / 94.91%
    Memory Usage: 14.2 MB / 13.00%
    """
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []

        output = []
        d = deque([(root, 0)])
        while d:
            current_node, level = d.popleft()

            if len(output) == level:
                output.append([])
            output[-1].append(current_node.val)

            if current_node.left is not None:
                d.append((current_node.left, level+1))
            if current_node.right is not None:
                d.append((current_node.right, level+1))

        for i in range(1, len(output), 2):
            output[i] = output[i][::-1]
        return output
