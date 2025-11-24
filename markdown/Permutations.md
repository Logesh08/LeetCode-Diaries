# [46. Permutations](https://leetcode.com/problems/permutations/description/)

Given an array <code>nums</code> of distinct integers, return all the possible <button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:r1k:" data-state="closed" class="">permutations</button>. You can return the answer in **any order** .

**Example 1:** 

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2:** 

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

**Example 3:** 

```
Input: nums = [1]
Output: [[1]]
```

**Constraints:** 

- <code>1 <= nums.length <= 6</code>
- <code>-10 <= nums[i] <= 10</code>
- All the integers of <code>nums</code> are **unique** .

---

## Solution

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        visited = [False] * n
        path = []
        def dfs():
            if len(path) == n:
                res.append(path.copy())
                return

            for idx in range(n):
                if not visited[idx]:
                    path.append(nums[idx])
                    visited[idx] = True
                    dfs()
                    path.pop()
                    visited[idx] = False

        dfs()
        return res
```