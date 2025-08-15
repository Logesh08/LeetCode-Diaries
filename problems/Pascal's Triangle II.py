from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]

        for _ in range(rowIndex):
            temp = [0] + ans + [0] 
            ans = [temp[i]+temp[i+1] for i in range(len(temp)-1)]

        return ans
    

print(Solution().getRow(0))
print(Solution().getRow(1))
print(Solution().getRow(2))
print(Solution().getRow(3))