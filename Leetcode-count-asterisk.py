# Solution for - https://leetcode.com/problems/count-asterisks/

class Solution:
    def countAsterisks(self, s: str) -> int:
        flag = False
        count = 0
        lens = len(s)

        for i in range(lens):
            # If we're in the pipe, then check only for closing pipe
            # else skip the characters comparison
            if flag:
                if s[i] == "|":
                    flag = False
            # If we're NOT in the pipe, then check for '*'
            else:
                if s[i] == "|":
                    flag = True
                    continue
                elif s[i] == "*":
                    count += 1

        return count
