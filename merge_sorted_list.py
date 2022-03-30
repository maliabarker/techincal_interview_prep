########################################################################################
#################################### !!WARNING!! #######################################
########################################################################################
# This does not run on here but does in leetcode, still figuring out how to do it here

'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

'''
INPUT: two lists of numbers
OUTPUT: a single combined list of numbers in ascending order
*example*
input: list1 = [1,2,4], list2 = [1,3,4]
output: [1,1,2,3,4,4]
'''

'''

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # instantiate two variables, a current node and a dummy node which will hold our list to be returned
        current = dummy = ListNode()
        # iterate over the values in each list while the values are not equal to None
        while list1 and list2:
            # check if the first value in list one is less than the first value in list 2
            if list1.val < list2.val:
                # if true, set the 'next' attribute of the current & dummy nodes to list 1
                current.next = list1
                # set 
                list1, current = list1.next, list1
            else:
                # else, value 2 is smaller and current's next attribute
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next


if __name__ == '__main__':
    test_obj = Solution()
    test_merge = test_obj.mergeTwoLists([1,2,4], [1,3,4])
    test_merge
