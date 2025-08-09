# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Using recursion

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def traverseAndGetDepth(node, depth):
            leftDepth = 0
            rightDepth = 0
            if node.left:
                leftDepth += traverseAndGetDepth(node.left, depth)
            if node.right:
                rightDepth += traverseAndGetDepth(node.right, depth)
            return depth + max(leftDepth,rightDepth)

        
        return traverseAndGetDepth(root,1)
    

# Using simple recursion, simple version

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    


# No iteration with deque

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        depth = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)
            depth += 1
        return depth


# No iteration with stack

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        ans = 0
        while stack:
            node, d = stack.pop()
            ans = max(ans, d)
            if node.left:  stack.append((node.left,  d + 1))
            if node.right: stack.append((node.right, d + 1))
        return ans