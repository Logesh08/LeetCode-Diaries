from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = False
        ans = 0
        for row in bank:
            count = row.count('1')
            if count > 0:
                if prev:
                    ans += prev * count
                prev = count
        return ans
                