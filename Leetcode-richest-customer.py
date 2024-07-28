# Solution for - https://leetcode.com/problems/richest-customer-wealth/


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for i in range(len(accounts)):
            temp = 0
            for j in range(len(accounts[i])):
                temp += accounts[i][j]
            if temp > max:
                max = temp
            
        return max
