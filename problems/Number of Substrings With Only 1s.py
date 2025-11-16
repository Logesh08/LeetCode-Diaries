class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        seqOnes = 0

        for c in s:
            if c == "1":
                seqOnes += 1
                res += seqOnes
            else:
                seqOnes = 0

        return res % MOD