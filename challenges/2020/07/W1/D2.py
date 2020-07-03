"""
Solution for July LeetCoding Challenges Week 1 Day 2: Binary Tree Level Order Traversal II

Definition for a binary tree node.
```
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
"""
from collections import defaultdict, deque


class Solution1:
    """
    Depth-first traversal while saving node values into dictionary by level.

    - Number of nodes: N
    - Space Complexity: O(N)
    - Time Complexity: O(N)

    Runtime: 52 ms / 11.66%
    Memory Usage: 14 MB / 86.62%
    """
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        output_dict = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            output_dict[level].append(node.val)
            if node.left is not None:
                queue.append((node.left, level+1))
            if node.right is not None:
                queue.append((node.right, level+1))

        output = []
        for i in sorted(output_dict.keys(), reverse=True):
            output.append(output_dict[i])

        return output



class Solution2:
    """
    Depth-first traversal but without the dictionary.

    - Number of nodes: N
    - Space Complexity: O(N)
    - Time Complexity: O(N)

    Runtime: 36 ms / 60.85%
    Memory Usage: 14.1 MB / 46.67%
    """
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        output = []
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if node.left is not None:
                queue.append((node.left, level+1))
            if node.right is not None:
                queue.append((node.right, level+1))

            if len(output) == level:
                output.append([])
            output[-1].append(node.val)

        return output[::-1]
