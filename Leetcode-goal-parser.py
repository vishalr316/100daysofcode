# Solution for - https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        for i in range(len(command)):
            if i >= len(command):
                return res
            else:
                if command[i] == 'G':
                    res += 'G'
                elif command[i] == '(':
                    if command[i+1] == ')':
                        res += 'o'
                        i += 2
                    else:
                        res += 'al'
                        i += 4
        return res
