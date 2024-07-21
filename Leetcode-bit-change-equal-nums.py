# Solution for - https://leetcode.com/contest/weekly-contest-407/problems/number-of-bit-changes-to-make-two-integers-equal/

class Solution:
    def minChanges(self, n: int, k: int) -> int:
        count = 0
        bin_k = bin(k)
        bin_k = bin_k[2:]
        
        bin_n = bin(n)
        bin_n = bin_n[2:]
        
        diff = abs(len(bin_k) - len(bin_n))
        
        if len(bin_k) < len(bin_n):
            bin_k = bin_k.zfill(len(bin_k) + diff)
        else:
            bin_n = bin_n.zfill(len(bin_n) + diff)
        
        len_n = len(bin_n)
        len_k = len(bin_k)
        
        if n == k:
            return count
        else:
            for i in range(len_n):
                if bin_n[i] == '1':
                    if bin_n[i] == bin_k[i]:
                        continue
                    else:
                        count += 1
                        bin_n = bin_n[:i] + '0' + bin_n[i+1:]
        if bin_n == bin_k:
            return count
        return -1
