# Solution for - https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if len(word) == 1:
            return word
        else:
            for i in range(len(word)):
                if ch == word[i]:
                    return word[i:0:-1] + word[0] + word[i+1:]
            return word
