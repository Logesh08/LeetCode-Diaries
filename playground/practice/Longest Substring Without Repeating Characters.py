class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        left = 0
        ans = 0
        for right in range(len(s)):
            while s[right] in hashMap and hashMap[s[right]] == 1:
                hashMap[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            hashMap[s[right]] = 1
        return ans
    
### Real optimal is using the index of others
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        ans = 0
        left = 0
        for right in range(len(s)):
            if s[right] in hashMap:
                left = max(hashMap[s[right]] + 1, left)
                # Here we take max for left because we need to reject, the value outside the window
            ans = max(ans, right - left + 1)
            hashMap[s[right]] = right
        return ans