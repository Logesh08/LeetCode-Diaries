# 4min 12 secs
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}

        for brace in s:
            if brace in brackets:
                if stack and stack[-1] == brackets[brace]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brace)

        return not stack