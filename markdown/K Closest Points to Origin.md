# [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/description/)

Given an array of <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a point on the **X-Y**  plane and an integer <code>k</code>, return the <code>k</code> closest points to the origin <code>(0, 0)</code>.

The distance between two points on the **X-Y**  plane is the Euclidean distance (i.e., <code>√(x<sub>1</sub> - x<sub>2</sub>)^2 + (y<sub>1</sub> - y<sub>2</sub>)^2</code>).

You may return the answer in **any order** . The answer is **guaranteed**  to be **unique**  (except for the order that it is in).

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg" style="width: 400px; height: 400px;">

```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
```

**Example 2:** 

```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```

**Constraints:** 

- <code>1 <= k <= points.length <= 10^4</code>
- <code>-10^4 <= x<sub>i</sub>, y<sub>i</sub> <= 10^4</code>

---

## Solution

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            heapq.heappush(minHeap, (x*x + y*y, x, y))

        res = []
        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res
```