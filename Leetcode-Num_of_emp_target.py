# Solution for - https://leetcode.com/problems/number-of-employees-who-met-the-target/

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res = 0
        for i in hours:
            if i >= target:
                res += 1
            else:
                continue
        return res
