# Solution for - https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        count = 0
        if len(s) != len(words):
            return False
        else:
            for i in range(len(s)):
                if s[i] == words[i][0]:
                    count += 1
                else:
                    return False
        return count == len(words)
