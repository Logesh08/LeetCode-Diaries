class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for v in "aeiou":
            if v in s:
                return True
        return False
        



class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(c in "aeiou" for c in s)