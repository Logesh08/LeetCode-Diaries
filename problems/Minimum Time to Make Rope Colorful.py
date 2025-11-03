from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        keep = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i]==colors[i-1]:
                res += min(keep, neededTime[i])
                keep = max(keep, neededTime[i])
            else:
                keep = neededTime[i]
        return res
        
        


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        keep = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i]==colors[i-1]:
                res += keep if keep < neededTime[i] else neededTime[i]
                keep = keep if keep > neededTime[i] else neededTime[i]
            else:
                keep = neededTime[i]
        return res