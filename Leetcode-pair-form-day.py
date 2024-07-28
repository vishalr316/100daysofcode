# Solution for - https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        sums = 0
        count = 0
        length = len(hours)
        
        if length == 1:
            return 0
        else:
            for i in range(length-1):
                for j in range(i+1, length):
                    sums = 0
                    sums = hours[i] + hours[j]
                    if sums % 24 == 0:
                        count += 1
        return count

