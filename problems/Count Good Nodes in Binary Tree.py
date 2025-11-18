# Definition for a binary tree node.
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
            if node.val > curMax:
                curMax = node.val
            if node.left:
                dfs(node.left, curMax)
            if node.right:
                dfs(node.right, curMax)

        dfs(root, root.val)

        return countOfGoodNodes