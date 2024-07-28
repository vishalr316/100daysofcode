# Solution for - https://leetcode.com/problems/score-of-a-string/description/


class Solution:
    def scoreOfString(self, s: str) -> int:
        abs_diff = 0
        res = 0

        if len(s) == 1:
            return ord(s)
        else:
            for i in range(0, len(s)-1):
                diff = abs(ord(s[i])-ord(s[i+1]))
                res += diff
        return res
