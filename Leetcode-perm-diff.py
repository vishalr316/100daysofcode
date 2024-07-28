# Solution for - https://leetcode.com/problems/permutation-difference-between-two-strings/

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        perm_sum = 0

        for i in range(len(s)):
            abs_diff = abs(i - t.index(s[i]))
            perm_sum += abs_diff
        return perm_sum
