# [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/description/)

You are given an <code>m x n</code> matrix <code>board</code> containing **letters**  <code>'X'</code> and <code>'O'</code>, **capture regions**  that are **surrounded** :

- **Connect** : A cell is connected to adjacent cells horizontally or vertically.
- **Region** : To form a region **connect every**  <code>'O'</code> cell.
- **Surround** : The region is surrounded with <code>'X'</code> cells if you can **connect the region ** with <code>'X'</code> cells and none of the region cells are on the edge of the <code>board</code>.

To capture a **surrounded region** , replace all <code>'O'</code>s with <code>'X'</code>s **in-place**  within the original board. You do not need to return anything.

**Example 1:** 

<div class="example-block">
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg" style="width: 367px; height: 158px;">
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

**Example 2:** 

<div class="example-block">
Input: board = [["X"]]

Output: [["X"]]

**Constraints:** 

- <code>m == board.length</code>
- <code>n == board[i].length</code>
- <code>1 <= m, n <= 200</code>
- <code>board[i][j]</code> is <code>'X'</code> or <code>'O'</code>.

---

## Solution

```python

```