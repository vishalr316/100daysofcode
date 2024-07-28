# Solution for - https://leetcode.com/problems/to-lower-case/

class Solution:
    def toLowerCase(self, s: str) -> str:
        lower_case = ""
        for i in s:
            o = ord(i)
            if o > 64 and o < 91:
                lower_case += chr(o + 32)
            else:
                lower_case += i
            
        return lower_case
