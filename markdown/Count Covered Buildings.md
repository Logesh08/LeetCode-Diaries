# [3531. Count Covered Buildings](https://leetcode.com/problems/count-covered-buildings/description/?envType=daily-question&envId=2025-12-11)

You are given a positive integer <code>n</code>, representing an <code>n x n</code> city. You are also given a 2D grid <code>buildings</code>, where <code>buildings[i] = [x, y]</code> denotes a **unique**  building located at coordinates <code>[x, y]</code>.

A building is **covered**  if there is at least one building in all **four**  directions: left, right, above, and below.

Return the number of **covered**  buildings.

**Example 1:** 

<img src="https://assets.leetcode.com/uploads/2025/03/04/telegram-cloud-photo-size-5-6212982906394101085-m.jpg" style="width: 200px; height: 204px;">

<div class="example-block">
Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]

Output: 1

Explanation:

- Only building <code>[2,2]</code> is covered as it has at least one building:

- above (<code>[1,2]</code>)
- below (<code>[3,2]</code>)
- left (<code>[2,1]</code>)
- right (<code>[2,3]</code>)

- Thus, the count of covered buildings is 1.

**Example 2:** 

<img src="https://assets.leetcode.com/uploads/2025/03/04/telegram-cloud-photo-size-5-6212982906394101086-m.jpg" style="width: 200px; height: 204px;">

<div class="example-block">
Input: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]

Output: 0

Explanation:

- No building has at least one building in all four directions.

**Example 3:** 

<img src="https://assets.leetcode.com/uploads/2025/03/16/telegram-cloud-photo-size-5-6248862251436067566-x.jpg" style="width: 202px; height: 205px;">

<div class="example-block">
Input: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]

Output: 1

Explanation:

- Only building <code>[3,3]</code> is covered as it has at least one building:

- above (<code>[1,3]</code>)
- below (<code>[5,3]</code>)
- left (<code>[3,2]</code>)
- right (<code>[3,5]</code>)

- Thus, the count of covered buildings is 1.

**Constraints:** 

- <code>2 <= n <= 10^5</code>
- <code>1 <= buildings.length <= 10^5 </code>
- <code>buildings[i] = [x, y]</code>
- <code>1 <= x, y <= n</code>
- All coordinates of <code>buildings</code> are **unique** .

---

## Solution

```python
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        res = 0
        maxRows = [0] * (n + 1)
        maxCols = [0] * (n + 1)
        minRows = [float("inf")] * (n + 1)
        minCols = [float("inf")] * (n + 1)

        for x, y in buildings:
            maxRows[x] = max(maxRows[x], y)
            minRows[x] = min(minRows[x], y)

            maxCols[y] = max(maxCols[y], x)
            minCols[y] = min(minCols[y], x)

        for x, y in buildings:
            if (minRows[x] < y < maxRows[x] and
                minCols[y] < x < maxCols[y]):
                res += 1

        return res
```