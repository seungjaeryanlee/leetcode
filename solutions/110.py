# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def recursive_is_balanced(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        if root is None:
            return (True, 0)
        
        left_balanced, left_height = self.recursive_is_balanced(root.left)
        right_balanced, right_height = self.recursive_is_balanced(root.right)

        if not left_balanced or not right_balanced:
            return False, -1
        if abs(left_height - right_height) > 1:
            return False, -1
        
        return True, max(left_height, right_height) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.recursive_is_balanced(root)[0]