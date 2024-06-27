# Solution for - https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing, isDecreasing = True, True
        lens = len(nums)

        for i in range(1, lens):
            if nums[i] < nums[i-1]:
                isIncreasing = False
            elif nums[i] > nums[i-1]:
                isDecreasing = False

        if (isIncreasing is False) and (isDecreasing is False):
                return False
        else:
            return True
