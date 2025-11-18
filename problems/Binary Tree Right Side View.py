# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import List, Optional


# BFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            rightMost = queue[-1]
            res.append(rightMost.val)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res
    


# DFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        def dfs(node: Optional[TreeNode], depth):
            if depth == len(res):
                res.append(0)

            res[depth] = node.val
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return res
    

# Smart ass dfs
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        def dfs(node: Optional[TreeNode], depth):
            if depth == len(res):
                res.append(node.val)

            if node.right:                  # By visiting right side first, we can garantee that we can
                dfs(node.right, depth + 1)  # append the first element itself!
            if node.left:
                dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res