"""
Solution for July LeetCoding Challenges Week 2 Day 6: Same Tree
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
    DFS traversal with a stack

    - Number of nodes: N
    - Space Complexity: O(N)
    - Time Complexity: O(N)

    Runtime: 32 ms / 77.09%
    Memory Usage: 13.7 MB / 78.16%
    """
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        d = deque([(p, q)])
        while d:
            p_, q_ = d.pop()
            if p_.val != q_.val:
                return False
            if p_.left is None and q_.left is not None:
                return False
            if p_.left is not None and q_.left is None:
                return False
            if p_.right is None and q_.right is not None:
                return False
            if p_.right is not None and q_.right is None:
                return False

            if p_.left is not None:
                d.append((p_.left, q_.left))
            if p_.right is not None:
                d.append((p_.right, q_.right))

        return True
