# [757. Set Intersection Size At Least Two](https://leetcode.com/problems/set-intersection-size-at-least-two/description/?envType=daily-question&envId=2025-11-19)

You are given a 2D integer array <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> represents all the integers from <code>start<sub>i</sub></code> to <code>end<sub>i</sub></code> inclusively.

A **containing set**  is an array <code>nums</code> where each interval from <code>intervals</code> has **at least two**  integers in <code>nums</code>.

- For example, if <code>intervals = [[1,3], [3,7], [8,9]]</code>, then <code>[1,2,4,7,8,9]</code> and <code>[2,3,4,8,9]</code> are **containing sets** .

Return the minimum possible size of a containing set.

**Example 1:** 

```
Input: intervals = [[1,3],[3,7],[8,9]]
Output: 5
Explanation: let nums = [2, 3, 4, 8, 9].
It can be shown that there cannot be any containing array of size 4.
```

**Example 2:** 

```
Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3
Explanation: let nums = [2, 3, 4].
It can be shown that there cannot be any containing array of size 2.
```

**Example 3:** 

```
Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
Output: 5
Explanation: let nums = [1, 2, 3, 4, 5].
It can be shown that there cannot be any containing array of size 4.
```

**Constraints:** 

- <code>1 <= intervals.length <= 3000</code>
- <code>intervals[i].length == 2</code>
- <code>0 <= start<sub>i</sub> < end<sub>i</sub> <= 10^8</code>

---

## Solution

```python
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda i: (i[1],-i[0]))
        p1 = -1
        p2 = -1

        for left, right in intervals:
            if left > p2:
                res += 2
                p1, p2 = right - 1, right
            elif p1 < left:
                res += 1
                p1, p2 = p2, right
            else:
                # Both lies in same point
                pass

        return res
```