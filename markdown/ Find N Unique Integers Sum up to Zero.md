# [1304. Find N Unique Integers Sum up to Zero](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/?envType=daily-question&envId=2025-09-07)

Given an integer <code>n</code>, return **any**  array containing <code>n</code> **unique**  integers such that they add up to <code>0</code>.

**Example 1:** 

```
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
```

**Example 2:** 

```
Input: n = 3
Output: [-1,0,1]
```

**Example 3:** 

```
Input: n = 1
Output: [0]
```

**Constraints:** 

- <code>1 <= n <= 1000</code>

---

## Solution

```python
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [0] if n%2 else []
        for i in range(1,n//2 + 1):
            ans.append(i)
            ans.append(-i)
        return ans
```