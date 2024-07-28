# Actual solution with in-place replacement
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_of_nums = 0
        for indx in range(len(nums)):0
            if nums[indx] != val:
                nums[num_of_nums] = nums[indx]
                num_of_nums += 1
        return num_of_nums



# My Solution for - https://leetcode.com/problems/remove-element/description/

##class Solution:
##    def removeElement(self, nums: List[int], val: int) -> int:
##        indexes = []
##        # get the indexes of the val in array.
##        for i in range(len(nums)):
##            if val == nums[i]:
##                indexes.append(i)
##
##        # Reverse the index so we dont have to worry about index out of range error on deleting these items from the original nums array
##        indexes.reverse()
##
##        # delete the elements and return the length of the array
##        for j in indexes:
##            del nums[j]
##            
##        return len(nums)
