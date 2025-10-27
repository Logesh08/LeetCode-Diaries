# [2125. Number of Laser Beams in a Bank](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/?envType=daily-question&envId=2025-10-25)

Anti-theft security devices are activated inside a bank. You are given a **0-indexed**  binary string array <code>bank</code> representing the floor plan of the bank, which is an <code>m x n</code> 2D matrix. <code>bank[i]</code> represents the <code>i^th</code> row, consisting of <code>'0'</code>s and <code>'1'</code>s. <code>'0'</code> means the cell is empty, while<code>'1'</code> means the cell has a security device.

There is **one**  laser beam between any **two**  security devices **if both**  conditions are met:

- The two devices are located on two **different rows** : <code>r<sub>1</sub></code> and <code>r<sub>2</sub></code>, where <code>r<sub>1</sub> < r<sub>2</sub></code>.
- For **each**  row <code>i</code> where <code>r<sub>1</sub> < i < r<sub>2</sub></code>, there are **no security devices**  in the <code>i^th</code> row.

Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/laser1.jpg" style="width: 400px; height: 368px;">

```
Input: bank = ["011001","000000","010100","001000"]
Output: 8
Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0^th row with any on the 3^rd row.
This is because the 2^nd row contains security devices, which breaks the second condition.
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/laser2.jpg" style="width: 244px; height: 325px;">

```
Input: bank = ["000","111","000"]
Output: 0
Explanation: There does not exist two devices located on two different rows.
```

**Constraints:** 

- <code>m == bank.length</code>
- <code>n == bank[i].length</code>
- <code>1 <= m, n <= 500</code>
- <code>bank[i][j]</code> is either <code>'0'</code> or <code>'1'</code>.

---

## Solution

```python
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = False
        ans = 0
        for row in bank:
            count = row.count('1')
            if count > 0:
                if prev:
                    ans += prev * count
                prev = count
        return ans
```