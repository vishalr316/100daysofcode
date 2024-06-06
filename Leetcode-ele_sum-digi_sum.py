# Solution for - https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit_sum = 0
        ele_sum = 0
        
        # getting the digit sum
        for i in range(len(nums)):
            if (nums[i] // 10) == 0:
                digit_sum += nums[i]
            else:
                n = nums[i]
                while (n // 10) > 0:
                    rem = n % 10
                    digit_sum += rem
                    n = n // 10
                digit_sum += (n % 10)
            
            # getting the element sum
            ele_sum += nums[i]

        return abs(ele_sum-digit_sum)
