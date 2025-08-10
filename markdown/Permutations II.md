# [47. Permutations II](https://leetcode.com/problems/permutations-ii/description/)

Given a collection of numbers, <code>nums</code>,that might contain duplicates, return all possible unique permutations **in any order** .

**Example 1:** 

```
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
```

**Example 2:** 

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Constraints:** 

- <code>1 <= nums.length <= 8</code>
- <code>-10 <= nums[i] <= 10</code>

---

## Solution

```python
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                # When we get our desired length, we can just return
                res.append(path[:])
                return

            for i in range(len(nums)):
                # Skip using the used ones
                if used[i]:
                    continue
                # Skip duplicate recursion at depth
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]: 
                    continue

                used[i] = True
                path.append([i])

                backtrack(path)
                # Here we will first fill all the elments like
                # [1,2,3,x] and start replacing from last like
                # [1,2,3,y], [1,2,3,z] and then go a step back
                # and do the same while there are unused

                path.pop()
                used[i] = False

        # Start with an empty [] which we will build each ans
        backtrack([])
        return res
```