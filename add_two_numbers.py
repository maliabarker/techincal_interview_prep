'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

'''
INPUT: two linked lists
OUTPUT: one linked list

EXAMPLE
input: l1 = [2,4,3], l2 = [5,6,4]
output: [7,0,8]
explanation: 342 + 465 = 807
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # add the first two nodes and any overflow
        # if the length of the resulting number is > 1 (there is overflow) then move it to the next addition
        # add the number of resulting addition to a new linked list
        
        # initialize a variable to stand in for the overflow
        overflow = 0
        # initialize a new linked list
        new_sum = dummy = ListNode()
        
        # iterate until the end of whichever list ends first
        while l1 or l2:
            num_1, num_2 = 0, 0
            if l1:
                num_1 = l1.val
                # move to next node in list
                l1 = l1.next
            if l2:
                num_2 = l2.val
                # move to next node in list
                l2 = l2.next
            
            this_sum = overflow + num_1 + num_2
            print(this_sum)
            
            # get single number by getting remainder of dividing by 10
            new_sum.next = ListNode(this_sum%10)
            # move on to next node in new sum 
            new_sum = new_sum.next
            # get overflow by dividing by ten
            overflow = this_sum//10
            
            # if there is overflow, assign the next node to the second number in int
            if overflow:
                new_sum.next = ListNode(overflow)
                
        # return the first (and only) node in the dummy linked list
        return dummy.next