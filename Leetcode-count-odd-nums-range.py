# Solution for - https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        if (low % 2) != 0:
            count += 1
            count += (high - low)//2
        else:
            count += (high - low)//2
            if (high % 2) != 0:
                count += 1
            
        return count
