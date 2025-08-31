from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = "+-*/"
        for token in tokens:
            if token in symbols:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    val = left + right
                elif token == '-':
                    val = left - right
                elif token == '*':
                    val = left * right
                else:
                    val = int(left / right)
                stack.append(val)
            else:
                stack.append(int(token))
        return stack.pop()