'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
'''

'''
INPUT: a singly linked list
OUTPUT: array of the middle node and all following nodes
EXAMPLE:
input: head = [1,2,3,4,5]
output: [3,4,5]
'''
'''FOR NODES OF SINGLY LINKED LIST'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class SolutionArr:
    def middleNode(self, head):
        # for an array of nodes
        nodes = [head]
        
        while nodes[-1].next:
            print(nodes[-1].next)
            nodes.append(nodes[-1].next)
        print(nodes)
        return nodes[ len(nodes) // 2 ]
 
            
class SolutionPoint:
    def middleNode(self, head):
        # for slow and fast pointers
        slow, fast = head, head
        
        while fast:
            # increment fast by two
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                # fast has reached the end of linked list
                # slow is on the middle point now
                break
            # increment slow by one
            slow = slow.next
        
        return slow