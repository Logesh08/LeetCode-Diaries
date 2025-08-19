# [679. 24 Game](https://leetcode.com/problems/24-game/description/)

You are given an integer array <code>cards</code> of length <code>4</code>. You have four cards, each containing a number in the range <code>[1, 9]</code>. You should arrange the numbers on these cards in a mathematical expression using the operators <code>['+', '-', '*', '/']</code> and the parentheses <code>'('</code> and <code>')'</code> to get the value 24.

You are restricted with the following rules:

- The division operator <code>'/'</code> represents real division, not integer division.

- For example, <code>4 / (1 - 2 / 3) = 4 / (1 / 3) = 12</code>.

- Every operation done is between two numbers. In particular, we cannot use <code>'-'</code> as a unary operator.

- For example, if <code>cards = [1, 1, 1, 1]</code>, the expression <code>"-1 - 1 - 1 - 1"</code> is **not allowed** .

- You cannot concatenate numbers together

- For example, if <code>cards = [1, 2, 1, 2]</code>, the expression <code>"12 + 12"</code> is not valid.

Return <code>true</code> if you can get such expression that evaluates to <code>24</code>, and <code>false</code> otherwise.

**Example 1:** 

```
Input: cards = [4,1,8,7]
Output: true
Explanation: (8-4) * (7-1) = 24
```

**Example 2:** 

```
Input: cards = [1,2,1,2]
Output: false
```

**Constraints:** 

- <code>cards.length == 4</code>
- <code>1 <= cards[i] <= 9</code>

---

## Solution

```python
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6
        cards = [float(card) for card in cards]

        def dfs(arr):
            if len(arr) == 1:
                return abs(arr[0] - 24) < EPS
            
            n = len(arr)
            for i in range(n):
                for j in range(i+1, n):
                    a, b = arr[i], arr[j]

                    remaining = [arr[k] for k in range(n) if k!=i and k!=j] # It's just whole list except the a and b, remaining ones

                    candidates = [a+b, a*b, a-b, b-a]

                    if abs(b) > EPS:
                        candidates.append(a/b)
                    if abs(a) > EPS:
                        candidates.append(b/a)

                    for val in candidates:
                        remaining.append(val)
                        if dfs(remaining):
                            return True
                        remaining.pop()

            return False
        
        return dfs(cards)
```