# [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

Given the <code>root</code> of a binary tree, return its maximum depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg" style="width: 400px; height: 277px;">

```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2:** 

```
Input: root = [1,null,2]
Output: 2
```

**Constraints:** 

- The number of nodes in the tree is in the range <code>[0, 10^4]</code>.
- <code>-100 <= Node.val <= 100</code>

---

## Solution

### Using recursion

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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
```
    

### Using simple recursion, simple version

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```
    


### No iteration with deque

```python
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
```


### No iteration with stack

```python
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
```