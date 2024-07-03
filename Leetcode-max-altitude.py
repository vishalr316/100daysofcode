# Solution for - https://leetcode.com/problems/find-the-highest-altitude/


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        sums = 0

        for i in range(len(gain)):
            sums += gain[i]
            res.append(sums)
        return max(res)
