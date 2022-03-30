'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

'''
INPUT: list of numbers and a target number
OUTPUT: integer value of the index in which the target number would be entered in numerical order
        OR if the target number is in the list already, return that index
*example*
input: [1, 3, 5, 6]
output: 2
'''

'''
iterate over each index in the list
    if the number at that index is greater than or equal to the target number, this is where is should go!
    return the index at that point
if you iterate over each number and there is still no return, that means the target is greater than all numbers in the list
SO the target should go at the end of the list 
'''

from cgi import test


class Solution:
    def searchInsert(self, nums, target) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)


'''
example:
input: number list = [1, 3, 5, 6], target = 2
iteration 1:
    i = 0
    nums[i] = 1 < target = 2 (no return)
iteration 2:
    i = 1
    nums[i] = 3 > target = 2, passes if statement test and return this i (1)
output: 1
'''

if __name__ == '__main__':
    test_obj = Solution()
    test_method = test_obj.searchInsert([1,3,5,6], 100000)
    print(test_method)
    test_array = [3, 2, 1]
    test_array.sort()
    print(test_array)