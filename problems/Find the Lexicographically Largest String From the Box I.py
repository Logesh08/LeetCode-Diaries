# LeetCode Problem 3403: Find the Lexicographically Largest String From the Box I
# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/


# You are given a string word, and an integer numFriends.

# Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

# word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
# All the split words are put into a box.
# Find the lexicographically largest string from the box after all the rounds are finished.

 

# Example 1:

# Input: word = "dbca", numFriends = 2

# Output: "dbc"

# Explanation: 

# All possible splits are:

# "d" and "bca".
# "db" and "ca".
# "dbc" and "a".
# Example 2:

# Input: word = "gggg", numFriends = 4

# Output: "g"

# Explanation: 

# The only possible split is: "g", "g", "g", and "g".

 

# Constraints:

# 1 <= word.length <= 5 * 10^3
# word consists only of lowercase English letters.
# 1 <= numFriends <= word.length





class Solution(object):
    def answerString(self, word, numFriends):
        n = len(word)
        if n == numFriends:
            return max(word)
        max_char = max(word)
        index = word.index(max_char)
        return word[:index + 1]