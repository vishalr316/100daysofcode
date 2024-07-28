# Solution for - https://leetcode.com/problems/repeated-substring-pattern

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lens = len(s)
        divisors = []

        for i in range(1, (lens//2)+1):
            if (lens % i) == 0:
                divisors.append(i)

        # Create string by multiplying the substring with the result of len//divisor
        # and match it with original string
        for j in divisors:
            if (s[:j] * (lens // j)) == s:
                return True
        return False
