# Solution for - https://leetcode.com/problems/sorting-the-sentence/


class Solution:
    def sortSentence(self, s: str) -> str:
        result = []
        inter = []
        first = 0
        indexes = []
        for i in range(len(s)):
            if s[i] == " ":
                inter.append(s[first:i-1])
                indexes.append(s[i-1])
                first = i+1
            elif i+1 == len(s):
                inter.append(s[first:i])
                indexes.append(s[i])

        for j in range(len(indexes)):
            result.append(inter[indexes.index(str(j+1))])
        return ' '.join(result)
