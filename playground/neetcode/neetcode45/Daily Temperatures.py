from typing import List

# 2min 30 secs
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                ind = stack[-1][0]
                res[ind] = i - ind
                stack.pop()
            stack.append([i, temp])

        return res