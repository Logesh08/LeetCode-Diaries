# Noob solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    

# Ultra noob solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap = {}
        for i in range(len(s)):
            hashMap[s[i]] = hashMap.get(s[i],0) + 1
            hashMap[t[i]] = hashMap.get(t[i],0) - 1
            for key in [s[i], t[i]]:
                if hashMap.get(key,-1) == 0:
                    del hashMap[key]
        if hashMap: return False
        return True
    
# God Pro solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
