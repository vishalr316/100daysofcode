# Solution for - https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def removeDuplicates(nums: list[int]) -> int:
        count = 0
        i=0
        position = None

        while (i < len(nums)-1) and (i+count < len(nums)):
        #for i in range(len(nums)-1):
            print("i= ",i)
            print("Nums is : ",nums)
            if (nums[i] == nums[i+1]):
                nums = nums[:i+1] + nums[i+2:] + [nums[i+1]]
                count += 1                
                print("Count = ",count)
                i -= 1
            # elif (nums[i] == nums[i+1]) and i == len(nums)-1:
                # nums = nums[:i] + nums[i+1:] +
            i += 1
            
        return len(nums)-count

res = removeDuplicates([1,1,2])
print("result: ",res)



# Working solution below
##
##        i,j=0,1
##        while i<=j and j<len(nums):
##            if nums[i]==nums[j]:
##                j+=1
##
##            else:
##                nums[i+1]=nums[j]
##                i+=1
##
##        return i+1

# Solution 2
##j = 1
##        for i in range(1, len(nums)):
##            if nums[i] != nums[i - 1]:
##                nums[j] = nums[i]
##                j += 1
##        return j
