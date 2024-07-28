# Solution for - https://leetcode.com/problems/decode-the-message/


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        res = ""
        key_substitute = []

        for i in range(len(key)):
            if key[i] == " ":
                continue
            elif key[i] not in key_substitute:
                key_substitute.append(key[i])

        for j in message:
            if j == " ":
                res += " "
            else:
                res += chr(key_substitute.index(j)+97)
        return res
