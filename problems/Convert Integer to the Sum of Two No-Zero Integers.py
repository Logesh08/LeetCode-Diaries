from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n+1):
            a = str(i)
            b = str(n - i)
            if "0" in a or "0" in b:
                continue
            return [i, n-i]
        return []
        


print(Solution().getNoZeroIntegers(5))