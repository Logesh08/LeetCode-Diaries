# [112. Path Sum](https://leetcode.com/problems/path-sum/description/)

Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return <code>true</code> if the tree has a **root-to-leaf**  path such that adding up all the values along the path equals <code>targetSum</code>.

A **leaf**  is a node with no children.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg" style="width: 500px; height: 356px;">

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg">

```
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
```

**Example 3:** 

```
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
```

**Constraints:** 

- The number of nodes in the tree is in the range <code>[0, 5000]</code>.
- <code>-1000 <= Node.val <= 1000</code>
- <code>-1000 <= targetSum <= 1000</code>

---

## Solution

### Using Dfs style recursion

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node, sum):
            sum += node.val
            if not node.left and not node.right:
                return sum == targetSum
            if node.right and node.left:
                return dfs(node.left, sum) or dfs(node.right, sum)
            if node.right:
                return dfs(node.right, sum)
            if node.left:
                return dfs(node.left, sum)
            

        return dfs(root,0)
```


### Simple recursion, super efficeient

```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return (self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val))
```