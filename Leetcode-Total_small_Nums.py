# Solution for - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            count = 0
            for j in nums:
                if i > j:
                    count += 1
            res.append(count)
        return res
