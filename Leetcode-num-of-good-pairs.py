# Solution for - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i] == nums[j]) and (i < j):
                    count += 1

        return count
