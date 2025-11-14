from typing import List

# 5mins 2 secs
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                leftSide = stack.pop()
                rightSide = stack.pop()
                if token == "+":
                    stack.append(rightSide + leftSide)
                elif token == '-':
                    stack.append(rightSide - leftSide)
                elif token == '*':
                    stack.append(rightSide * leftSide)
                else:
                    stack.append(int(rightSide / leftSide))
                

        return stack[0]