"""
Solution for July LeetCoding Challenges Week 2 Day 2: Maximum Width of Binary Tree
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
    Traverse with BFS while saving column index

    - Number of nodes: N
    - Space Complexity: O(N)
    - Time Complexity: O(N)

    Runtime: 40 ms / 79.96%
    Memory Usage: 14.1 MB / 72.73%
    """
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        max_width = 0
        left_index = None
        left_level = None
        d = deque([(root, 0, 0)])
        while d:
            node, level, index = d.popleft()

            # BFS
            if node.left is not None:
                d.append((node.left, level + 1, index * 2))
            if node.right is not None:
                d.append((node.right, level + 1, index * 2 + 1))

            # Compute width
            if left_level != level:
                left_level = level
                left_index = index
            elif max_width < index - left_index:
                max_width = index - left_index

        return max_width + 1 # 0 and 3 is 4 apart, not 3
