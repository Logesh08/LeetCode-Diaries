from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        return bin(n)[2:]

print(Solution.productQueries(5))