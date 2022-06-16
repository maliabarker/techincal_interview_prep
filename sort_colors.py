'''
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, 
white, and blue, respectively.
'''

'''
INPUT: Array of numbers (0, 1, 2 for red, white, blue)
OUTPUT: Array of sorted numbers
EXAMPLE:
input: [2,0,2,1,1,0]
output: [0,0,1,1,2,2]
'''

from turtle import left


class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i = 0
        # num_i = 0
        # # go over three times checking for each number (0, 1, 2)
        # while i < 3:
        #     # go over each number in the list
        #     while num_i < len(nums):
# PROBLEM: HOW TO CHECK THAT IT IS THE END?
        #         # if number in list is equal to the number we are checking for (0, 1, 2)
        #         # then move to back of list
        #         if nums[num_i] == i:
        #             nums += [nums.pop(num_i)]
        #         else: 
        #         # increment number list index by one so it will keep going
        #             num_i += 1
        #     # increment target number index so it keeps going
        #     i += 1
        #     # set number list index back to 0
        #     num_i = 0

        # we are going to move 0 to the left, 2 to the right, and 1 will stay is place
        # so 1 will eventually be in the middle

        left_pointer = 0
        right_pointer = len(nums)-1
        current_pointer = 0

        while current_pointer <= right_pointer:
            # check if the currently iterated number is 0, 1, or 2
            if nums[current_pointer] < 1:
                # if the current number is 0

                # set current number to the start (left most number)
                nums[current_pointer] = nums[left_pointer]

                # set the start (left_pointer) to the current number
                nums[left_pointer] = nums[current_pointer]

                # increment the left pointer (start)
                left_pointer += 1
                # increment the current pointer
                current_pointer += 1
            elif nums[current_pointer] == 1:
                # if the current number is 1 do nothing
                current_pointer += 1
            else:
                # if the current number is 2
                # move the current number to the end (left pointer)
                nums[right_pointer] = nums[current_pointer]
                # move whatever is at the end (left_pointer) to the current number position
                nums[current_pointer] = nums[right_pointer]
                # decrement the left_pointer so it will not count the last number
                right_pointer -= 1
        
