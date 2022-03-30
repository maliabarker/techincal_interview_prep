'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead 
have the result be placed in the first part of the array nums. More formally, 
if there are k elements after removing the duplicates, then the first k elements of nums should hold the 
final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.
'''

'''
INPUT: list of numbers with duplicates
OUTPUT: length of the non duplicate numbers and the list with non duplicate numbers up to index of length determined
*example*
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
'''

from cgi import test


class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        x = 1
        while i+x in range(len(nums) - 1):
        #     # if the number at this index and the next are different (not equal to eachother)
        #     # then assign the next index to this unique number
        #     if nums[i]!=nums[i+1]:
        #         nums[x] = nums[i+1]
        #         # increment x by one to move to the next index for this modified list
        #         x+=1
        # return(x, nums)

            # if the current number equals the next number
            if nums[i] == nums[i+x]:
                # search for a unique number by incrementing x and adding that to the index
                while nums[i] == nums[i+x]:
                    x += 1
                # when the for loop breaks this means the value of i+x is unique
                print(x, nums[i+x])
                # assign the next index of the list to this new increment
                nums[i+1] = nums[i+x]
            i += 1
        print(nums)
        return i+1, nums
        
test_obj = Solution()
test_method = test_obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(test_method)