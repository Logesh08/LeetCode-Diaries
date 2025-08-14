class Solution:
    def largestGoodInteger(self, num: str) -> str:
        freqCount = 0
        prev = ""
        ans = -1

        for c in num:
            if c == prev:
                freqCount += 1
            else:
                if freqCount >= 3:
                    print(prev,ans)
                    ans = max(int(prev), ans)
                freqCount = 1
            prev = c
        if freqCount >= 3:
            ans = max(int(prev), ans)

        return str(ans) * 3 if ans != -1 else ""

print(Solution().largestGoodInteger("6777133339"))