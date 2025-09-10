# [1733. Minimum Number of People to Teach](https://leetcode.com/problems/minimum-number-of-people-to-teach/description/?envType=daily-question&envId=2025-09-10)

On a social network consisting of <code>m</code> users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer <code>n</code>, an array <code>languages</code>, and an array <code>friendships</code> where:

- There are <code>n</code> languages numbered <code>1</code> through <code>n</code>,
- <code>languages[i]</code> is the set of languages the <code>i^​​​​​​th</code>​​​​ user knows, and
- <code>friendships[i] = [u<sub>​​​​​​i</sub>​​​, v<sub>​​​​​​i</sub>]</code> denotes a friendship between the users <code>u^​​​​​<sub>​​​​​​i</sub></code>​​​​​ and <code>v<sub>i</sub></code>.

You can choose **one**  language and teach it to some users so that all friends can communicate with each other. Return <i data-stringify-type="italic">the</i> <i>**minimum**  </i><i data-stringify-type="italic">number of users you need to teach.</i>
Note that friendships are not transitive, meaning if <code>x</code> is a friend of <code>y</code> and <code>y</code> is a friend of <code>z</code>, this doesn't guarantee that <code>x</code> is a friend of <code>z</code>.

**Example 1:** 

```
Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
Output: 1
Explanation: You can either teach user 1 the second language or user 2 the first language.
```

**Example 2:** 

```
Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
Output: 2
Explanation: Teach the third language to users 1 and 3, yielding two users to teach.
```

**Constraints:** 

- <code>2 <= n <= 500</code>
- <code>languages.length == m</code>
- <code>1 <= m <= 500</code>
- <code>1 <= languages[i].length <= n</code>
- <code>1 <= languages[i][j] <= n</code>
- <code>1 <= u<sub>​​​​​​i</sub> < v<sub>​​​​​​i</sub> <= languages.length</code>
- <code>1 <= friendships.length <= 500</code>
- All tuples <code>(u<sub>​​​​​i, </sub>v<sub>​​​​​​i</sub>)</code> are unique
- <code>languages[i]</code> contains only unique values

---

## Solution
```python
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        users = set()
        languages = [set(lang) for lang in languages]

        for u, v in friendships:
            if languages[u-1].isdisjoint(languages[v-1]):
                users.add(u)
                users.add(v)

        if not users:
            return 0
        
        res = float("inf")

        for lang in range(1,n+1):
            alradyKnow = sum([1 for user in users if lang in languages[user-1]])
            toTeach = len(users) - alradyKnow
            res = min(res, toTeach)

        return res
```