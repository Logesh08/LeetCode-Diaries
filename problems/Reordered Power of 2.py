# My initial approach

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = list(str(n))
        digits.sort()
        perms = []
        used = [False] * len(digits)

        def backtrack(path):
            if len(path) == len(digits):
                perms.append(path[:])
                return
            
            for i in range(len(digits)):
                if used[i] or (not path and digits[i] == '0'):
                    continue
                if i > 0 and digits[i] == digits[i-1] and not used[i-1]:
                    continue

                path.append(digits[i])
                used[i] = True

                backtrack(path)

                used[i] = False
                path.pop()



        backtrack([])

        for perm in perms:
            num = int(''.join(perm))
            if num > 0 and (num & (num - 1)) == 0:
                return True

        return False
    

# Optimzed variation
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = sorted(str(n))
        for i in range(30):  # 2^30 is the largest power of 2 within the range of 10^9
            if sorted(str(1 << i)) == digits:
                return True
        return False