class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = list(map(int,s))
        right = len(digits)
        while right > 2:
            for i in range(right-1):
                digits[i] = (digits[i] + digits[i+1]) % 10
            right -= 1
        return digits[0] == digits[1]

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [ord(ch) - 48 for ch in s]  # 5–10x faster than int() calls
        right = len(digits)
        while right > 2:
            for i in range(right-1):
                digits[i] = (digits[i] + digits[i+1]) % 10
            right -= 1
        return digits[0] == digits[1]


print(Solution().hasSameDigits("3902"))