# Solution for - https://leetcode.com/problems/sum-of-all-subset-xor-totals/


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.helper(nums, 0, 0)

    def helper(self, nums, index, currValue):
        if index == len(nums):
            return currValue
        return self.helper(nums, index+1, currValue ^ nums[index]) + self.helper(nums, index+1, currValue)
