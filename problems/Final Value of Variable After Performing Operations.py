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
    

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for opr in operations:
            if opr[0]=='-' or opr[-1]=='-':
                ans -= 1
            else:
                ans += 1
        return ans