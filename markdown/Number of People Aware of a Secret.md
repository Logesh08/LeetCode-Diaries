# [2327. Number of People Aware of a Secret](https://leetcode.com/problems/number-of-people-aware-of-a-secret/description/?envType=daily-question&envId=2025-09-09)

On day <code>1</code>, one person discovers a secret.

You are given an integer <code>delay</code>, which means that each person will **share**  the secret with a new person **every day** , starting from <code>delay</code> days after discovering the secret. You are also given an integer <code>forget</code>, which means that each person will **forget**  the secret <code>forget</code> days after discovering it. A person **cannot**  share the secret on the same day they forgot it, or on any day afterwards.

Given an integer <code>n</code>, return the number of people who know the secret at the end of day <code>n</code>. Since the answer may be very large, return it **modulo**  <code>10^9 + 7</code>.

**Example 1:** 

```
Input: n = 6, delay = 2, forget = 4
Output: 5
Explanation:
Day 1: Suppose the first person is named A. (1 person)
Day 2: A is the only person who knows the secret. (1 person)
Day 3: A shares the secret with a new person, B. (2 people)
Day 4: A shares the secret with a new person, C. (3 people)
Day 5: A forgets the secret, and B shares the secret with a new person, D. (3 people)
Day 6: B shares the secret with E, and C shares the secret with F. (5 people)
```

**Example 2:** 

```
Input: n = 4, delay = 1, forget = 3
Output: 6
Explanation:
Day 1: The first person is named A. (1 person)
Day 2: A shares the secret with B. (2 people)
Day 3: A and B share the secret with 2 new people, C and D. (4 people)
Day 4: A forgets the secret. B, C, and D share the secret with 3 new people. (6 people)
```

**Constraints:** 

- <code>2 <= n <= 1000</code>
- <code>1 <= delay < forget <= n</code>

---

## Solution

```python
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MODULO = 10**9 + 7

        dp = [0] * (n+1)
        dp[1] = 1

        activeSpreaders = 0
        for day in range(2,n+1):
            if day > delay:
                activeSpreaders = activeSpreaders + dp[day-delay]
            if day > forget:
                activeSpreaders = activeSpreaders - dp[day-forget]
            dp[day] = activeSpreaders
        ans = sum(dp[n-forget+1:n+1])

        return ans % MODULO
```