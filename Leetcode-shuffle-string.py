# Solution for - https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ""
        leng = len(s)

        for i in range(leng):
            ind = indices.index(i)
            res += s[ind]
        return res
