# Solution for - https://leetcode.com/problems/truncate-sentence/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        count = 0

        for i in range(len(s)):
            if count == k:
                return s[0:i-1]
            elif s[i] == ' ':
                count += 1
        
        return s
