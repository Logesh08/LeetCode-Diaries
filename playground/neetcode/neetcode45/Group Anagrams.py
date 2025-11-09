from collections import defaultdict
from typing import List

# 4min 11 secs
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for ch in word:
                key[ord(ch) - ord('a')] += 1
            hashMap[tuple(key)].append(word)

        return list(hashMap.values())




class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            hashMap[key].append(word)

        return list(hashMap.values())