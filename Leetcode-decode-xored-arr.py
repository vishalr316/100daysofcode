# Solution for - https://leetcode.com/problems/decode-xored-array/description/


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        count = 0

        for i in encoded:
            res.append(res[count] ^ i)
            count += 1
        return res

