class Solution:
    def maximum69Number (self, num: int) -> int:
        digit_list = list(str(num))
        for i in range(len(digit_list)):
            if digit_list[i] == '6':
                digit_list[i] = '9'
                return int(''.join(digit_list))
        return num
    
# Pure numberic approach
class Solution:
    def maximum69Number(self, num: int) -> int:
        n = num
        pos = -1  # to store position of leftmost 6
        i = 0     # digit index from right (0 = ones place)

        while n > 0:
            digit = n % 10
            if digit == 6:
                pos = i  # update position of last seen 6
            n //= 10
            i += 1

        if pos == -1:  # no 6 found
            return num
        return num + 3 * (10 ** pos)
    
print(Solution().maximum69Number(9669))