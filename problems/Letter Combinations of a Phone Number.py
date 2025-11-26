from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        numberMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        cur = []
        def dfs(i: int) -> None:
            if i == len(digits):
                res.append(cur.copy())
                return
            
            for char in numberMap[digits[i]]:
                cur.append(char)
                dfs(i + 1)
                cur.pop()

        dfs(0)

        return res