import re
from typing import List
from collections import defaultdict



# Best solution
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        def case_hash(s):
            return s.lower()
        
        def vowel_hash(s):
            return s.lower().replace('e', 'a').replace('i', 'a').replace('o', 'a').replace('u', 'a')
        
        
        exact = set(wordlist)
        case = defaultdict()
        vowl = defaultdict()
        for w in wordlist:
            c = case_hash(w)
            if c not in case: case[c] = w
            v = vowel_hash(w)
            if v not in vowl: vowl[v] = w
        
        def correct(w):
            if w in exact: return w
            c = case_hash(w)
            if c in case: return case[c]
            v = vowel_hash(w)
            if v in vowl: return vowl[v]
            return ''
                    
        return [correct(q) for q in queries]
            




## WORST SOLUTION
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        def normalizeWord(word: str):
            return re.sub(r"[aeiou]", ".", word.lower())

        ans = []
        wordSet = set(wordlist)
        lowerWordSet = set([word.lower() for word in wordlist])
        vowelFixList = [normalizeWord(word) for word in wordlist]

        for query in queries:
            if query in wordSet:
                ans.append(query)
            elif query.lower() in lowerWordSet:
                for word in wordlist:
                    if word.lower() == query.lower():
                        ans.append(word)
                        break
            elif normalizeWord(query) in vowelFixList:
                ans.append(wordlist[vowelFixList.index(normalizeWord(query))])
            else:
                ans.append("")

        return ans