# Solution for - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        #lens = len(piles) // 3
        start = 0
        end = len(piles)
        piles.sort()
        res = 0

        while start < end:
            end -= 2
            res += piles[end]
            start += 1
        return res
