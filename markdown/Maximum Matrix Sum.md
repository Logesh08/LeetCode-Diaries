# [1975. Maximum Matrix Sum](https://leetcode.com/problems/maximum-matrix-sum/description/?envType=daily-question&envId=2026-01-05)

You are given an <code>n x n</code> integer <code>matrix</code>. You can do the following operation **any**  number of times:

- Choose any two **adjacent**  elements of <code>matrix</code> and **multiply**  each of them by <code>-1</code>.

Two elements are considered **adjacent**  if and only if they share a **border** .

Your goal is to **maximize**  the summation of the matrix's elements. Return the **maximum**  sum of the matrix's elements using the operation mentioned above.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex1.png" style="width: 401px; height: 81px;">

```
Input: matrix = [[1,-1],[-1,1]]
Output: 4
<b>Explanation:</b> We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex2.png" style="width: 321px; height: 121px;">

```
Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
<b>Explanation:</b> We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
```

**Constraints:** 

- <code>n == matrix.length == matrix[i].length</code>
- <code>2 <= n <= 250</code>
- <code>-10^5 <= matrix[i][j] <= 10^5</code>

---

## Solution

```python
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        maxSum = 0
        minAbs = float("inf")
        noOfNeg = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val = matrix[i][j]
                maxSum += abs(val)
                minAbs = min(minAbs, abs(val))
                if val < 0:
                    noOfNeg += 1

        return maxSum if noOfNeg % 2 == 0 else maxSum - (2 * minAbs)
```