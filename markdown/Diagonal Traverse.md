# [498. Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse/description/)

Given an <code>m x n</code> matrix <code>mat</code>, return an array of all the elements of the array in a diagonal order.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg" style="width: 334px; height: 334px;">

```
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
```

**Example 2:** 

```
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
```

**Constraints:** 

- <code>m == mat.length</code>
- <code>n == mat[i].length</code>
- <code>1 <= m, n <= 10^4</code>
- <code>1 <= m * n <= 10^4</code>
- <code>-10^5 <= mat[i][j] <= 10^5</code>

---

## Solution

```python
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        i = j = 0
        direction = 1
        for _ in range(m*n):
            res.append(mat[i][j])
            if direction == 1:
                if j == n-1:
                    i += 1
                    direction = -1
                elif i == 0:
                    j += 1
                    direction = -1
                else:
                    i -= 1
                    j += 1
            else:
                if i == m-1:
                    j += 1
                    direction = 1
                elif j == 0:
                    i += 1
                    direction = 1
                else:
                    i += 1
                    j -= 1
        return res
```