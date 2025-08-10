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
                # Skip duplicate recursion at any depth
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