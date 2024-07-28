# Solution for - https://leetcode.com/problems/length-of-last-word/description/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        letter_count = 0
        for i in s[::-1]:
            if i == ' ' and letter_count != 0:
                break
            elif i == ' ':
                continue
            else:
                letter_count += 1
        return letter_count
