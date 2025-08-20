# [1277. Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/?envType=daily-question&envId=2025-08-20)

Given a <code>m * n</code> matrix of ones and zeros, return how many **square**  submatrices have all ones.

**Example 1:** 

```
Input: matrix =
[
 [0,1,1,1],
 [1,1,1,1],
 [0,1,1,1]
]
Output: 15
Explanation: 
There are **10**  squares of side 1.
There are **4**  squares of side 2.
There is  **1**  square of side 3.
Total number of squares = 10 + 4 + 1 = **15** .
```

**Example 2:** 

```
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are <b>6</b> squares of side 1.  
There is **1**  square of side 2. 
Total number of squares = 6 + 1 = <b>7</b>.
```

**Constraints:** 

- <code>1 <= arr.length<= 300</code>
- <code>1 <= arr[0].length<= 300</code>
- <code>0 <= arr[i][j] <= 1</code>

---

## Solution

```python
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        ans = 0

        for i in range(col):
            ans += matrix[0][i]

        for i in range(1, row):
            ans += matrix[i][0]

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 1:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) # It's just top, left, and top-left
                    ans += matrix[i][j]

        return ans
```