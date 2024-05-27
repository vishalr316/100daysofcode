# Python3 Solution for leetcode problem - https://leetcode.com/problems/concatenation-of-array/description/


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        else:
            ans = list(nums) + list(nums)
            return ans
