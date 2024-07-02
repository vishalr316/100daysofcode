# Solution for - https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        res = []
        lens = len(sentence)

        if lens < 26:
            return False
        else:
            for i in sentence:
                if len(res) == 26:
                    return True
                elif i not in res:
                    res.append(i)
        if len(res) == 26:
            return True
        return False
