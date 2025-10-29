class Solution:
    def smallestNumber(self, n: int) -> int:
        binOfN = bin(n)[2:]
        return int("1" * len(binOfN), 2)