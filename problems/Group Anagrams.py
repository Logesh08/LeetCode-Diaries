from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            hashKey = ''.join(sorted(s))
            hashMap.setdefault(hashKey, []).append(s)

        #return [[s for s in hashMap[key]] for key in hashMap.keys()]
        return list(hashMap.values())