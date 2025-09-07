from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [0] if n%2 else []
        for i in range(1,n//2 + 1):
            ans.append(i)
            ans.append(-i)

print(Solution().sumZero(2))