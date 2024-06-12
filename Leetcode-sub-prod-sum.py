# Solution for - https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sums = 0
        mod = 0

        while n//10 > 0:
            mod = n % 10
            prod *= mod
            sums += mod
            n = n // 10
        prod *= n
        sums += n
        return prod-sums
