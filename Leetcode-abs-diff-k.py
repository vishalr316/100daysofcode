# Solution for - https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        lens = len(nums)
        
        if lens == 2:
            if abs(nums[0] - nums[1]) == k:
                return 1
            else:
                return 0
        else:
            for i in range(lens-1):
                for j in range(i+1, lens):
                    if abs(nums[i] - nums[j]) == k:
                        count += 1

        return count
