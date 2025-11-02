class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        window = {}

        for ch in t:
            target[ch] = target.get(ch, 0) + 1

        need = len(target)
        have = 0

        start = end = -1
        minLen = float("inf")

        left = 0
        for right in range(len(s)):
            ch = s[right]
            if ch in target:
                window[ch] = window.get(ch, 0) + 1
            
                if window[ch] == target[ch]:
                    have += 1

            while have == need:
                if (right - left + 1) < minLen:
                    start = left
                    end = right
                    minLen = right - left + 1
                ch = s[left]
                if ch in window:
                    window[ch] -= 1
                    if window[ch] == target[ch] - 1:
                        have -= 1
                left += 1
                

        return s[start:end+1] if minLen != float("inf") else ""