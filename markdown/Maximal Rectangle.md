# [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/description/?envType=daily-question&envId=2026-01-11)

Given a <code>rows x cols</code>binary <code>matrix</code> filled with <code>0</code>'s and <code>1</code>'s, find the largest rectangle containing only <code>1</code>'s and return its area.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg" style="width: 402px; height: 322px;">

```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
```

**Example 2:** 

```
Input: matrix = [["0"]]
Output: 0
```

**Example 3:** 

```
Input: matrix = [["1"]]
Output: 1
```

**Constraints:** 

- <code>rows == matrix.length</code>
- <code>cols == matrix[i].length</code>
- <code>1 <= rows, cols <= 200</code>
- <code>matrix[i][j]</code> is <code>'0'</code> or <code>'1'</code>.