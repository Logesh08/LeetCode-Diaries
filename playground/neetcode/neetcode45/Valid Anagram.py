# 3 mins 45 secs
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashMap1 = {}
        hashMap2 = {}
        for i in range(len(s)):
            hashMap1[s[i]] = hashMap1.get(s[i], 0) + 1
            hashMap2[t[i]] = hashMap2.get(t[i], 0) + 1

        ## Alrernate solution
        return hashMap1 == hashMap2

        for key in hashMap1.keys():
            if key not in hashMap2 or hashMap1[key] != hashMap2[key]:
                return False
            
        return True