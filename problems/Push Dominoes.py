# LeetCode Problem 838: Push Dominoes
# https://leetcode.com/problems/push-dominoes/



# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

# You are given a string dominoes representing the initial state where:

# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.

 

# Example 1:

# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.
# Example 2:


# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
 

# Constraints:

# n == dominoes.length
# 1 <= n <= 10^5
# dominoes[i] is either 'L', 'R', or '.'.





# I tried solving like this, but was stuck somewhere, got some help from the AI

# Doesn't work

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        n = len(dominoes)

        right = left = 0

        while right < n:
            if dominoes[right] == 'L':
                while left < right:
                    dominoes[left] = 'L'
                    left += 1
            if dominoes[right] == 'R':
                left = right
                right += 1
                while right < n and dominoes[right] == '.':
                    right += 1
                if dominoes[right] == 'L':
                    cur = right
                    while left < right and left != right:
                        dominoes[left] = 'R'
                        dominoes[right] = 'L'
                        left += 1
                        right -= 1

                    right = left = cur
                else:
                    while left < right:
                        dominoes[left] = 'R'
                        left += 1

            right += 1

        return ''.join(dominoes)
    



# Ohh my god my program was almost correct just missed out two things
# Dint add a continue and an extra check

# Beats 90+% of the submissions

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        n = len(dominoes)

        right = left = 0

        while right < n:
            if dominoes[right] == 'L':
                while left < right:
                    dominoes[left] = 'L'
                    left += 1
            if dominoes[right] == 'R':
                left = right
                right += 1
                while right < n and dominoes[right] == '.':
                    right += 1
                if right < n and dominoes[right] == 'L': # Dint check this
                    cur = right
                    while left < right and left != right:
                        dominoes[left] = 'R'
                        dominoes[right] = 'L'
                        left += 1
                        right -= 1

                    right = left = cur
                else:
                    while left < right:
                        dominoes[left] = 'R'
                        left += 1
                continue # Didnt add this
                # Adding continue because I have already added right+1, 
                # else withot continue I can do right - 1

            right += 1

        return ''.join(dominoes)
    




# Realised that I made a mistake after seeing this solution only,
# Which AI made based on my approach

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        n = len(dominoes)
        left = 0
        right = 0

        while right < n:
            # Case 1: we hit an 'L' with no intervening 'R'
            if dominoes[right] == 'L':
                # everything from left…right-1 must fall to 'L'
                while left < right:
                    dominoes[left] = 'L'
                    left += 1

            # Case 2: we hit an 'R'
            if dominoes[right] == 'R':
                # mark the start of a potential R… segment
                left = right
                # scan forward to find the next force
                right += 1
                while right < n and dominoes[right] == '.':
                    right += 1

                # if that next force is an 'L', we have R…L
                if right < n and dominoes[right] == 'L':
                    lo, hi = left, right
                    # push inwards from both ends
                    while lo < hi:
                        dominoes[lo] = 'R'
                        dominoes[hi] = 'L'
                        lo += 1
                        hi -= 1
                    # set both pointers to just past that L
                    left = right + 1
                else:
                    # otherwise (R…R or R…end), everything from left…right-1 → 'R'
                    fill_to = right if right < n else n
                    while left < fill_to:
                        dominoes[left] = 'R'
                        left += 1
                # now continue from exactly the force we just processed
                continue

            right += 1

        return "".join(dominoes)
