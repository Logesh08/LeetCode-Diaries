# [2438. Range Product Queries of Powers](https://leetcode.com/problems/range-product-queries-of-powers/description/?envType=daily-question&envId=2025-08-11)

Given a positive integer <code>n</code>, there exists a **0-indexed**  array called <code>powers</code>, composed of the **minimum**  number of powers of <code>2</code> that sum to <code>n</code>. The array is sorted in **non-decreasing**  order, and there is **only one**  way to form the array.

You are also given a **0-indexed**  2D integer array <code>queries</code>, where <code>queries[i] = [left<sub>i</sub>, right<sub>i</sub>]</code>. Each <code>queries[i]</code> represents a query where you have to find the product of all <code>powers[j]</code> with <code>left<sub>i</sub> <= j <= right<sub>i</sub></code>.

Return an array <code>answers</code>, equal in length to <code>queries</code>, where <code>answers[i]</code> is the answer to the <code>i^th</code> query. Since the answer to the <code>i^th</code> query may be too large, each <code>answers[i]</code> should be returned **modulo**  <code>10^9 + 7</code>.

**Example 1:** 

```
Input: n = 15, queries = [[0,1],[2,2],[0,3]]
Output: [2,4,64]
Explanation:
For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
Answer to 2nd query: powers[2] = 4.
Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
Each answer modulo 10^9 + 7 yields the same answer, so [2,4,64] is returned.
```

**Example 2:** 

```
Input: n = 2, queries = [[0,0]]
Output: [2]
Explanation:
For n = 2, powers = [2].
The answer to the only query is powers[0] = 2. The answer modulo 10^9 + 7 is the same, so [2] is returned.
```

**Constraints:** 

- <code>1 <= n <= 10^9</code>
- <code>1 <= queries.length <= 10^5</code>
- <code>0 <= start<sub>i</sub> <= end<sub>i</sub> < powers.length</code>

---

## Solution

Wrong Approach, but almost there, but here constraints are pretty huge
```python
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
```

Now Imma try in correct apprach...
```python
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
```