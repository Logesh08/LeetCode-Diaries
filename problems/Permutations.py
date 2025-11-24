from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        path = []
        def dfs(i):
            if len(path) == n:
                res.append(path.copy())
                return

            for idx in range(n):
                if i != idx:
                    path.append(nums[idx])
                    dfs(idx)
                    path.pop()

        dfs(0)
        return res