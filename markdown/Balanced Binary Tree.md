# [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)

Given a binary tree, determine if it is <button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:rs:" data-state="closed" class="">**height-balanced** </button>.

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def heightOfNode(node):
            if not node:
                return 0
            
            left = heightOfNode(node.left)
            if left == -1:
                return -1
            
            right = heightOfNode(node.right)
            if right == -1:
                return -1
            
            if abs(right - left) > 1:
                return - 1

            return 1 + max(right, left)

        return heightOfNode(root) != -1
```