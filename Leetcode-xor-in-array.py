# Solution for - https://leetcode.com/problems/xor-operation-in-an-array/


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor_res = 0
        nums = []
        for i in range(n):
            formula = start + 2*i
            nums.append(formula)
            xor_res = xor_res ^ formula
        return xor_res
