# Solution for - https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution:
    def replaceDigits(self, s: str) -> str:
        lens = len(s)
        res = ""

        if lens == 1:
            return s
        else:
            for i in range(1, lens, 2):
                res += self.shift(s[i-1], s[i])
            if lens % 2 == 1:
                res += s[-1]
        return res

    def shift(self, char, ind):
        return char + chr(ord(char)+int(ind))
