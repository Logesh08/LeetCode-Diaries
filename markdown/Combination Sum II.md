

---

## Solution

```python
class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        nums.sort()
        cur: List[int] = []
        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(i + 1, total + nums[i])
            cur.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i+1, total)

        dfs(0, 0)
        return res
```