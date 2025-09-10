from typing import List


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