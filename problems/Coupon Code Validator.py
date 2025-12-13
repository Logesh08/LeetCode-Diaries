from typing import List


class Solution:
    def validateCoupons(self, codes: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        res = []
        catogries = {"electronics", "grocery", "pharmacy", "restaurant"}
        priority = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        def isValidCode(code: str) -> bool:
            for c in code:
                if not (c.isalnum() or c == "_"):
                    return False
            return not not code

        for code, line, active in zip(codes, businessLine, isActive):
            if active and line in catogries and isValidCode(code):
                res.append((priority[line], code))

        res.sort()

        return [code for sortKey, code in res]