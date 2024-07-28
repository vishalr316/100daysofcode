# Solution for - https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description/

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []
        chars = s[0]
        nums = [s[1],s[-1]]

        #for i in chars:
        while chars <= s[-2]:
            n1 = int(s[1])
            n2 = int(s[-1])

            while n1 <= n2:
                res.append(chars + str(n1))
                n1 += 1
            chars = chr(ord(chars)+1)

        return res
