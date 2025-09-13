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
    


class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        freq_map = defaultdict(int)
        for char in s:
            freq_map[char] += 1
        
        vowel_max = 0
        consonant_max = 0
        vowels = "aeiou"
        for key, value in freq_map.items():
            if key in vowels:
                if value > vowel_max:
                    vowel_max = value
            else:
                if value > consonant_max:
                    consonant_max = value
        
        return vowel_max + consonant_max