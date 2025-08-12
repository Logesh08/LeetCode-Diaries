from typing import List

# Wrong Approach, but almost there, but here constraints are pretty huge

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        bits = bin(n)[2:]
        power = [1] if bits[-1] == '1' else [] 
        ans = []

        dp = [1]
        for i in range(len(bits)-1):
            dp.append(dp[-1] * 2)
            if bits[i - len(bits)] == '1':
                power.append(dp[-1])

        for start,end in queries:
            cur = 1
            for i in range(start,end+1):
                cur *= power[i]
            ans.append(cur)


        return ans



# Now Imma try in correct apprach...

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # First define this when question mentions the `return modulo`
        MOD = 10**9 + 7

        # exponents of set bits, ascending (since powers array is sorted non-decreasing)
        exps = [i for i in range(31) if (n >> i) & 1]

        # prefix sums of exponents
        prefix = [0]
        for e in exps:
            prefix.append(prefix[-1] + e)

        # product of 2^{e_l}..2^{e_r} = 2^{sum(e_l..e_r)}
        ans = []
        for l,r in queries:
            summ = prefix[r+1] - prefix[l]
            ans.append(pow(2,summ,MOD))

        return ans