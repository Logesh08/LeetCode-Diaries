from typing import List, Set










class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        wordSet.discard(beginWord)
        
        stack = [beginWord]
        res = 1

        def generateWords(word: str) -> set:
            possible = set()
            wordBuff = list(word)

            for i in range(len(wordBuff)):
                original = wordBuff[i]
                for j in range(26):
                    ch = chr(ord('a') + j)
                    if ch == original:
                        continue
                    wordBuff[i] = ch
                    cand = ''.join(wordBuff)
                    if cand in wordSet:
                        possible.add(cand)
                wordBuff[i] = original
            return possible

        while stack:
            tempStack = []
            while stack:
                word = stack.pop()
                nextLevel = generateWords(word)
                if endWord in nextLevel:
                    return res + 1
                for w in nextLevel:
                    wordSet.remove(w)
                    tempStack.append(w)
            res += 1
            stack = tempStack
        return 0