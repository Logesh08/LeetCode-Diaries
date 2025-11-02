class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        targetMap = {}
        windowMap = {}
        for c in s1:
            targetMap[c] = targetMap.get(c, 0) + 1
        
        left = 0
        for right in range(len(s1)-1, len(s2)):
            