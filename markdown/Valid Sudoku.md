# [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)

Determine if a<code>9 x 9</code> Sudoku boardis valid.Only the filled cells need to be validated**according to the following rules** :

- Each rowmust contain thedigits<code>1-9</code> without repetition.
- Each column must contain the digits<code>1-9</code>without repetition.
- Each of the nine<code>3 x 3</code> sub-boxes of the grid must contain the digits<code>1-9</code>without repetition.

**Note:** 

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentionedrules.

**Example 1:** 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" style="height: 250px; width: 250px;">

```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

**Example 2:** 

```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the **5**  in the top left corner being modified to **8** . Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

**Constraints:** 

- <code>board.length == 9</code>
- <code>board[i].length == 9</code>
- <code>board[i][j]</code> is a digit <code>1-9</code> or <code>'.'</code>.

---

## Solution
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if (num in rows[i] or
                    num in cols[j] or
                    num in boxes[(i // 3) * 3 + (j // 3)]):
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[(i // 3) * 3 + (j // 3)].add(num)
        return True
```