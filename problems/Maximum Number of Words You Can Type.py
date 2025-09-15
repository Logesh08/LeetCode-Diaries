class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        for word in text.split():
            if not set(word).intersection(brokenLetters):
                ans += 1
        return ans



class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        for word in text.split():
            canBeTyped  = True
            for char in brokenLetters:
                if char in word:
                    canBeTyped = False
                    break
            if canBeTyped:
                ans += 1
        return ans
