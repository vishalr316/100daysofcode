# Solution for - https://leetcode.com/problems/maximum-odd-binary-number/


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        lens = len(s)
        count = 0

        for i in range(lens):
            if s[i] == '1':
                count += 1
        if lens == count or count == 0:
            return s
        elif count == 1:
            return '0' * (lens-count) + '1'
        else:
            return '1' * (count-1) + '0' * (lens-count) + '1'
