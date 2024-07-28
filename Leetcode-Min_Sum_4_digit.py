# Solution for - https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:
    def minimumSum(self, num: int) -> int:
        n1, n2 = "", ""
        nums = str(num)
        sort_num = sorted(nums)
        n1 = sort_num[0]+sort_num[2]
        n2 = sort_num[1]+sort_num[3]

        return int(n1)+int(n2)
