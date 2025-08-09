# [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

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

## Solutions

### Using recursion
```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(a,b):
            if a == None and b == None:
                return True
            if a == None or b == None or a.val != b.val:
                return False
            return isMirror(a.left,b.right) and isMirror(a.right,b.left)
        
        if not root:
            return False

        return isMirror(root.left,root.right)
```

### Using loop
```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([(root.left,root.right)])

        while queue:
            a,b = queue.popleft()
            if a == None and b == None:
                continue
            if a == None or b == None or a.val != b.val:
                return False
            
            queue.append((a.left,b.right))
            queue.append((a.right,b.left))

        return True
```