# Solution for - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lens = len(nums)
        for i in range(lens-1):
            for j in range(i+1,lens):
                if (nums[i]+nums[j]) == target:
                    return [i,j]
        return -1
