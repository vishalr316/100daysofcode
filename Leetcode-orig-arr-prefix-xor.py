# Solution for - https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]

        if len(pref) >= 2:
            for i in range(1, len(pref)):
                res.append(pref[i-1] ^ pref[i])
        else:
            return res
        return res
