'''Given an integer x, return true if x is palindrome integer.'''

'''
GIVEN : an integer of any length
OUTPUT : a boolean value (true or false) that determines if given integer is a palindrome 

* example *
Input: x = 121
Output: true
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        —given—
        :type x: int

        —returned—
        :rtype: bool
        """

        # convert the integer into a list of integers ->
        #   iterate over each single integer within the given int
        #   append to a list
        num_list = [i for i in str(x)]
        
        # instantiate i equal to zero
        i = 0

        # iterate through the list of numbers until you get to the middle (which is the length of the list divided by 2)
        while i <= len(num_list)/2:
            # check the number in this index
            # check the number at the end of the list minus the index 
            # add one to the index number because the list starts at 0
            #   so a list of length 15 will really have a last index of 14
            if num_list[i] == num_list[len(num_list) - (i+1)]:
                # if the numbers equal eachother, this is a palindrome so far and we continue
                i += 1
            else:
                # else, they are not equal and this number is therefore not a palindrome
                # return false
                return False
        # if we get to the end of the list of number (or the middle as stated above),
        # and it passes each time then the whole number is a palindrome and we return true
        return True