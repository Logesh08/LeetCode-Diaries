# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Using BFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            l = []
            cur = []
            while queue:
                node: TreeNode = queue.popleft()
                if node:
                    cur.append(node.left)
                    cur.append(node.right)
                    l.append(node.val)
            if cur:
                queue.extend(cur)
                res.append(l)

        return res
    


# Space complexity upgrade
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            l = []
            for _ in range(len(queue)):
                node: TreeNode = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    l.append(node.val)
            if l:
                res.append(l)

        return res
    


# Using DFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res: List[List[int]] = []

        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return
            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res