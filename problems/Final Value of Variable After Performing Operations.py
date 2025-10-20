# Final Value of Variable After Performing Operations

from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for opr in operations:
            if "-" in opr:
                ans -= 1
            else:
                ans += 1
        return ans