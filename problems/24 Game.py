from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6
        cards = [float(card) for card in cards]

        def dfs(arr):
            if len(arr) == 1:
                return abs(arr[0] - 24) < EPS
            
            n = len(arr)
            for i in range(n):
                for j in range(i+1, n):
                    a, b = arr[i], arr[j]

                    remaining = [arr[k] for k in range(n) if k!=i and k!=j] # It's just whole list except the a and b, remaining ones

                    candidates = [a+b, a*b, a-b, b-a]

                    if abs(b) > EPS:
                        candidates.append(a/b)
                    if abs(a) > EPS:
                        candidates.append(b/a)

                    for val in candidates:
                        remaining.append(val)
                        if dfs(remaining):
                            return True
                        remaining.pop()

            return False
        
        return dfs(cards)




# Bellow are inital tries of imporper solutions

# Iinitial version which will not work..
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        ans = []
        n = len(cards)
        used = [False] * n

        sol = []

        def doMath(data):
            if len(data) == 1:
                sol.append(data[0] == 24)
                return
            
            a, b = data.pop(), data.pop()

            doMath(data + [a+b])
            doMath(data + [a-b])
            doMath(data + [a*b])
            if b != 0:
                doMath(data + [a/b])


        def backtrack(path):
            if len(path) == n:
                ans.append(path[:])
                doMath(path[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                path.append(cards[i])
                backtrack(path)
                path.pop()
                used[i] = False


        backtrack([])

        return any(sol)
    



# Updated the doMath()

def doMath(data,sol):
    if len(data) == 1:
        sol.append(abs(data[0] - 24) < 1e-6)
        return

    EPS = 1e-6
    a = data.pop()
    b = data.pop()
    
    doMath(data + [a + b])
    doMath(data + [a * b])

    doMath(data + [a - b])
    doMath(data + [b - a])

    if abs(b) > EPS:
        doMath(data + [a / b])
    if abs(a) > EPS:
        doMath(data + [b / a])


