# Solution for - https://leetcode.com/problems/find-the-number-of-good-pairs-i/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0
        len1 = len(nums1)
        len2 = len(nums2)

        for i in range(len1):
            for j in range(len2):
                if (nums1[i] % (nums2[j]*k)) == 0:
                    count += 1
        
        return count
