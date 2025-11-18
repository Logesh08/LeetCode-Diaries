# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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