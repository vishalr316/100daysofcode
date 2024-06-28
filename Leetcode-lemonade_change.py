# Solution for - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10:0, 20:0}
        lens = len(bills)
        for i in range(lens):
            if bills[i] == 5:
                change[5] += 1
            elif bills[i] == 10:
                if change[5] >= 1:
                    change[5] -= 1
                    change[10] += 1
                else:
                    return False
            elif bills[i] == 20:
                if change[10] >= 1:
                    if change[5] >= 1:
                        change[5] -= 1
                        change[10] -= 1
                        change[20] += 1
                    else:
                        return False
                elif change[5] >= 3:
                    change[5] = change[5] - 3
                    change[20] += 1
                else:
                    return False

        return True
