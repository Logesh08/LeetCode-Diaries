# [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/)

Given a binary tree, determine if it is <button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:r7o:" data-state="closed" class="">**height-balanced** </button>.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg" style="width: 342px; height: 221px;">

```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg" style="width: 452px; height: 301px;">

```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

**Example 3:** 

```
Input: root = []
Output: true
```

**Constraints:** 

- The number of nodes in the tree is in the range <code>[0, 5000]</code>.
- <code>-10^4 <= Node.val <= 10^4</code>


---

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        
        return 1 + min(self.minDepth(root.left),self.minDepth(root.right))
```   


### Without using recursion
```python

from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 1)])
        while q:
            node, d = q.popleft()
            if not node.left and not node.right:
                return d
            if node.left:
                q.append((node.left, d + 1))
            if node.right:
                q.append((node.right, d + 1))
```