# Solution for - https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        if ruleKey == 'type':
            index = 0
        elif ruleKey == 'color':
            index = 1
        elif ruleKey == 'name':
            index = 2

        for i in range(len(items)):
            if items[i][index] == ruleValue:
                count += 1
        return count
