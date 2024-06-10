# Solution for - https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        word_count = {}
        for i in range(len(sentences)):
            word_count[i] = 1
            for j in range(len(sentences[i])):
                if sentences[i][j] == ' ':
                    word_count[i] += 1
        return max(word_count.values())
