# Solution for - https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary: List[int]) -> float:
        mins = maxs = salary[0]
        lens = len(salary)
        res = 0

        for i in range(lens):
            res += salary[i]
            if salary[i] < mins:
                mins = salary[i]
            if salary[i] > maxs:
                maxs = salary[i]
        return (res-mins-maxs)/(lens-2)
