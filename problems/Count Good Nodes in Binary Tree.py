# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Using DFS
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        countOfGoodNodes = 0

        def dfs(node: TreeNode, curMax: int):
            if node.val >= curMax:
                nonlocal countOfGoodNodes
                countOfGoodNodes += 1
                curMax = node.val
            if node.left:
                dfs(node.left, curMax)
            if node.right:
                dfs(node.right, curMax)

        dfs(root, root.val)

        return countOfGoodNodes
    

# Using BFS
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        countOfGoodNodes = 0
        queue = deque()
        queue.append([root, root.val])

        while queue:
            for _ in range(len(queue)):
                node, curMax = queue.popleft()
                if node.val >= curMax:
                    countOfGoodNodes += 1
                    curMax = node.val

                if node.left:
                    queue.append([node.left, curMax])
                if node.right:
                    queue.append([node.right, curMax])

        return countOfGoodNodes