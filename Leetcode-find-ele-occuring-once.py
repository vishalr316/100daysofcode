# Solution for - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            s = s ^ i
        return s
