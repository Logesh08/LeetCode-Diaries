# [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)

A **path**  in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once** . Note that the path does not need to pass through the root.

The **path sum**  of a path is the sum of the node's values in the path.

Given the <code>root</code> of a binary tree, return the maximum **path sum**  of any **non-empty**  path.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg" style="width: 322px; height: 182px;">

```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg">

```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

**Constraints:** 

- The number of nodes in the tree is in the range <code>[1, 3 * 10^4]</code>.
- <code>-1000 <= Node.val <= 1000</code>

---

## Solution

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            
            leftMax = max(0, dfs(node.left))
            rightMax = max(0, dfs(node.right))

            res[0] = max(res[0], node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
```