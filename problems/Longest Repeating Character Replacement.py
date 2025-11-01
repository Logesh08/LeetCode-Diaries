class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        ans = 0
        left = 0
        maxFreq = 0
        for right in range(len(s)):
            hashMap[s[right]] = hashMap.get(s[right], 0) + 1
            maxFreq = max(hashMap[s[right]], maxFreq)
            while (right - left + 1) - maxFreq > k:
                hashMap[s[left]] -= 1
                left += 1
            ans = max(right - left + 1, ans)
        return ans