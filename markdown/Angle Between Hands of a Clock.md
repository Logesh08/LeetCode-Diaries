# [1344. Angle Between Hands of a Clock](https://leetcode.com/problems/angle-between-hands-of-a-clock/description/)

Given two numbers, <code>hour</code> and <code>minutes</code>, return the smaller angle (in degrees) formed between the <code>hour</code> and the <code>minute</code> hand.

Answers within <code>10^-5</code> of the actual value will be accepted as correct.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2019/12/26/sample_1_1673.png" style="width: 300px; height: 296px;">

```
Input: hour = 12, minutes = 30
Output: 165
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2019/12/26/sample_2_1673.png" style="width: 300px; height: 301px;">

```
Input: hour = 3, minutes = 30
Output: 75
```

**Example 3:** 
<img alt="" src="https://assets.leetcode.com/uploads/2019/12/26/sample_3_1673.png" style="width: 300px; height: 301px;">

```
Input: hour = 3, minutes = 15
Output: 7.5
```

**Constraints:** 

- <code>1 <= hour <= 12</code>
- <code>0 <= minutes <= 59</code>

---

## Solution

```python
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = hour % 12
        normalizeHour = (5 * hour) + (5 * (minutes / 60))
        segments = abs(minutes - normalizeHour)
        angle =  6 * segments
        return min(angle, 360 - angle)
```