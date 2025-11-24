# [90. Subsets II](https://leetcode.com/problems/subsets-ii/description/)

Given an integer array <code>nums</code> that may contain duplicates, return all possible <button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:r1k:" data-state="closed" class="">subsets</button> (the power set).

The solution set **must not**  contain duplicate subsets. Return the solution in **any order** .

**Example 1:** 

```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**Example 2:** 

```
Input: nums = [0]
Output: [[],[0]]
```

**Constraints:** 

- <code>1 <= nums.length <= 10</code>
- <code>-10 <= nums[i] <= 10</code>

---

## Solution

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        nums.sort()
        path = []
        def dfs(i):
            res.append(path.copy())
            
            for idx in range(i, n):
                if idx > i and nums[idx] == nums[idx - 1]:
                    continue
                path.append(nums[idx])
                dfs(idx + 1)
                path.pop()

        dfs(0)
        return res
```