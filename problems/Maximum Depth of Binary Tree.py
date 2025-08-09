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
    

