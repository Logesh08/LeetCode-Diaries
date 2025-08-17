# [837. New 21 Game](https://leetcode.com/problems/new-21-game/description/?envType=daily-question&envId=2025-08-17)

Alice plays the following game, loosely based on the card game **"21"** .

Alice starts with <code>0</code> points and draws numbers while she has less than <code>k</code> points. During each draw, she gains an integer number of points randomly from the range <code>[1, maxPts]</code>, where <code>maxPts</code> is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets <code>k</code> **or more points** .

Return the probability that Alice has <code>n</code> or fewer points.

Answers within <code>10^-5</code> of the actual answer are considered accepted.

**Example 1:** 

```
Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.
```

**Example 2:** 

```
Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.
```

**Example 3:** 

```
Input: n = 21, k = 17, maxPts = 10
Output: 0.73278
```

**Constraints:** 

- <code>0 <= k <= n <= 10^4</code>
- <code>1 <= maxPts <= 10^4</code>

--- 

## Solution

```python
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts - 1:
            return 1.0
        
        dp = [1.0] + [0.0]*n

        window = dp[0]
        ans = 0.0

        for i in range(1,n+1):
            dp[i] = window / maxPts

            if i < k:
                window += dp[i]
            else:
                ans += dp[i]

            if i-maxPts >= 0 and i-maxPts < k:
                window -= dp[i - maxPts]

        return ans
```