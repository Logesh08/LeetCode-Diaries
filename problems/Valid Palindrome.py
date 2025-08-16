# My initial version

class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = []
        for c in s:
            if c.isalpha() or c.isdigit():
                test.append(c.lower())
        return test == test[::-1]
    
# Realised I could use isalnum
class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = []
        for c in s:
            if c.isalnum():
                test.append(c.lower())
        return test == test[::-1]
    

# What if we use reverse comparison??
class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = []
        for c in s:
            if c.isalnum():
                test.append(c.lower())

        for i in range(len(test)//2):
            if test[i] != test[len(test)-1-i]:
                return False
        return True
# Still same performance, no significat impovement



# Lets try another version
class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = [c for c in s.lower() if c.isalnum()]
        return test == test[::-1]
    


# Improvement of previous one
class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = [c for c in s.lower() if c.isalnum()]
        n = len(test)
        for i in range(n//2):
            if test[i] != test[n-1-i]:
                return False
        return True
    

# Wow I finally beat 99% of the submissions where I stareted from 
