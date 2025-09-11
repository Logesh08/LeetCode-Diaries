class Solution:
    def sortVowels(self, s: str) -> str:
        buffer = []
        ans = []

        for c in s:
            if c.lower() in "aeiou":
                ans.append(0)
                buffer.append(c)
            else:
                ans.append(c)

        buffer.sort(key= lambda x: ord(x))

        for i in range(len(s)-1,-1,-1):
            if ans[i] == 0:
                ans[i] = buffer.pop()

        return ''.join(ans)