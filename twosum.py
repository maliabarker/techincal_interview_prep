'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

'''
GIVEN : list of integers and a target integer
OUTPUT : list containing two indices whose sum equals the given target number

* example *
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        —given—
        :type nums: List[int]
        :type target: int

        —returned—
        :rtype: List[int]
        """
        
        # dictionary with index as key and number as value
        num_dict = {}
        for i in range(len(nums)):
            num_dict[i] = nums[i]
        
        i = 0
        while i in range(len(nums)):
            # subtract num from target
            target_num = target - nums[i]
            # check if result is in dict values
            if target_num in num_dict.values():
                # also check that result is not the same as current num
                if list(num_dict.values()).index(target_num) is not i:
                    # if conditionals are met, return this num and the index of target num which will be the key
                    return [i, list(num_dict.values()).index(target_num)]
            # if nothing found, move onto next num
            i += 1

if __name__ == '__main__':
    test_object = Solution()
    test_method = test_object.twoSum([2,7,11,15], 9)
    print(test_method)
