# Solution for - https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = 0
        for i in moves:
            if i == "L":
                count += 2
            elif i == "R":
                count -= 2
            elif i == "U":
                count += 3
            elif i == "D":
                count -= 3
        
        if count is 0:
            return True
        else:
            return False
