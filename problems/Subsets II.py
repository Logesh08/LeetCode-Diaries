from typing import List


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