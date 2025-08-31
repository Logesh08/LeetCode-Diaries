from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for ind,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                resInd = stack.pop()[1]
                res[resInd] = ind - resInd
            stack.append([temp,ind])

        return res
    


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        hottest = temperatures[-1]

        for i in range(len(temperatures)-2,-1,-1):
            if temperatures[i] >= hottest:
                hottest = temperatures[i]
                continue
            j = i + 1
            while temperatures[j] <= temperatures[i]:
                j += res[j]
            res[i] = j - 1


        return res
    

Solution().dailyTemperatures([1,2,3,4])