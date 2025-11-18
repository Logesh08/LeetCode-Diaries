# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional



# using BFS
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((root, float("-inf"), float("inf")))

        while queue:
            for _ in range(len(queue)):
                node, low, high = queue.popleft()
                if node:
                    if not (low < node.val < high):
                        return False
                    queue.append((node.left, low, node.val))
                    queue.append((node.right, node.val, high))

        return True


# using DFS
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode], low: int, heigh: int):
            if not node:
                return True
            if not (low < node.val < heigh): # Not valid
                return False
            return dfs(node.left, low, node.val) and  dfs(node.right, node.val, heigh)

        return dfs(root, float("-inf"), float("inf"))