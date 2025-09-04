# [853. Car Fleet](https://leetcode.com/problems/car-fleet/description/)

There are <code>n</code> cars at given miles away from the starting mile 0, traveling to reach the mile <code>target</code>.

You are given two integer arrays<code>position</code> and <code>speed</code>, both of length <code>n</code>, where <code>position[i]</code> is the starting mile of the <code>i^th</code> car and <code>speed[i]</code> is the speed of the <code>i^th</code> car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A **car fleet**  is a single car or a group of cars driving next to each other. The speed of the car fleet is the **minimum**  speed of any car in the fleet.

If a car catches up to a car fleet at the mile <code>target</code>, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

**Example 1:** 

<div class="example-block">
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

Output: 3

Explanation:

- The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at <code>target</code>.
- The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
- The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches <code>target</code>.

**Example 2:** 

<div class="example-block">
Input: target = 10, position = [3], speed = [3]

Output: 1

Explanation:
There is only one car, hence there is only one fleet.

**Example 3:** 

<div class="example-block">
Input: target = 100, position = [0,2,4], speed = [4,2,1]

Output: 1

Explanation:

- The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
- Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches <code>target</code>.

**Constraints:** 

- <code>n == position.length == speed.length</code>
- <code>1 <= n <= 10^5</code>
- <code>0 < target <= 10^6</code>
- <code>0 <= position[i] < target</code>
- All the values of <code>position</code> are **unique** .
- <code>0 < speed[i] <= 10^6</code>

---

## Solution

Stack based approach:
```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)):
            time = (target-position[i]) / speed[i]
            stack.append([position[i],time])

        stack.sort(key= lambda x: x[0])

        ans = 1
        cur = stack.pop()

        while stack:
            top = stack.pop()
            if top[1] > cur[1]:
                ans += 1
                cur = top
            else:
                continue

        return ans
```

No Stack approach:
```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos_to_speed = {pos : spd for pos, spd in zip(position, speed)}
        max_time = 0
        res = 0
        position = sorted(position)

        for i in range(len(position) - 1, -1, -1):
            pos = position[i]
            time = (target - pos) / pos_to_speed[pos]

            if max_time >= time:
                continue
            max_time = time
            res += 1

        return res 
```