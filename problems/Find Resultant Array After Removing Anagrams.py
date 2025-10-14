from typing import Counter, List


class Solution(object):
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        freq = [Counter(w) for w in words]
        ans = [words[0]]
        for i in range(1, n):
            if freq[i] != freq[i - 1]:
                ans.append(words[i])
        return ans
    

    
class Solution(object):
    def removeAnagrams(self, words):
        ans = [words[0]]
        for i in range(1, len(words)):
            a, b = sorted(words[i]), sorted(ans[-1])
            if a != b:
                ans.append(words[i])
        return ans