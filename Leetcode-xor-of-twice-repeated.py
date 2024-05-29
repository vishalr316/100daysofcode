# Solution for - https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/description/


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        count = {}
        xor_value = 0
        for i in nums:
            if i in count:
                xor_value = xor_value ^ i
            else:
                count[i] = 1
        return xor_value
