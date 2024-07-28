# Solution for - https://leetcode.com/contest/biweekly-contest-135/problems/find-the-winning-player-in-coin-game/

class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        count = 0
        
        while (x >= 1) and (y >= 4):
            count += 1
            x -= 1
            y -= 4
        if (count % 2) != 0:
            return "Alice"
        else:
            return "Bob"
