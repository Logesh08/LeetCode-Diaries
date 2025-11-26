# [79. Word Search](https://leetcode.com/problems/word-search/description/)

Given an <code>m x n</code> grid of characters <code>board</code> and a string <code>word</code>, return <code>true</code> if <code>word</code> exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" style="width: 322px; height: 242px;">

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg" style="width: 322px; height: 242px;">

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

**Example 3:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/word3.jpg" style="width: 322px; height: 242px;">

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

**Constraints:** 

- <code>m == board.length</code>
- <code>n = board[i].length</code>
- <code>1 <= m, n <= 6</code>
- <code>1 <= word.length <= 15</code>
- <code>board</code> and <code>word</code> consists of only lowercase and uppercase English letters.

**Follow up:**  Could you use search pruning to make your solution faster with a larger <code>board</code>?

---

## Solution

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in range(n)]

        res = [False]

        def dfs(i, j, chInd):
            if res[0]:
                return
            if word[chInd] != board[i][j]:
                return
            if chInd == len(word) - 1:
                res[0] = True
                return
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dx = i + x
                dy = j + y
                if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy]:
                    visited[i][j] = True
                    dfs(dx, dy, chInd + 1)
                    visited[i][j] = False
                    

        for i in range(n):
            for j in range(m):
                dfs(i, j, 0)
                if res[0]:
                    return True

        return res[0]
```