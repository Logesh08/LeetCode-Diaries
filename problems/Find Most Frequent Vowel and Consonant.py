from collections import defaultdict


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowFreq = consFreq = defaultdict(int)
        vowFreqMax = consFreqMax = 0
        for c in s:
            if c in "aeiou":
                vowFreq[c] += 1
                vowFreqMax = max(vowFreqMax, vowFreq[c])
            else:
                consFreq[c] += 1
                consFreqMax = max(consFreqMax, consFreq[c])
        return vowFreqMax + consFreqMax