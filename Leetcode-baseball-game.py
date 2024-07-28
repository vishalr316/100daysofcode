# Solution for - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lens = len(operations)
        record = []

        for i in range(lens):
            temp = None
            if operations[i] == '+':
                temp = record[-1] + record[-2]
                record.append(temp)
            elif operations[i] == 'D':
                temp = record[-1] * 2
                record.append(temp)
            elif operations[i] == 'C':
                record.pop()
            else:
                record.append(int(operations[i]))
        
        return sum(record)
