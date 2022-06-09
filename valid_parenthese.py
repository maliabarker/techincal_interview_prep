'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''
'''
INPUT: string containing only different types of parentheses
OUTPUT: boolean value indicating if parentheses have matching closing pair in correct order
*example*
input: "()[]{}"
output: true
input: "(]"
output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        # create dictionary that has opening parentheses as key and matching closing as value
        parentheses = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        # instantiate i as 0
        i = 0
        # iterate over each charcter in the given string by 2
        for i in range(0, len(s), 2):
            stack = []
            '''SOLUTION 1'''
            # check if the amount of characters is odd or even by dividing by two and getting remainder
                # if remainder is 0 that means its divisible by two and therefore even, which will have a number of characters possible to match
            if len(s)%2 != 0:
                return False
            # check if the next charcter is the dict value of the current character (aka the matching closing character)
            if s[i+1] != parentheses[s[i]]:
                # if the next character is not the matching closing charcter OR
                # if the remainder of the length divided by 2 is more than 0 (meaning there is not enough charcters to make matches)
                # return false
                return False
            '''SOLUTION 2'''
            # check if tuple is in .items which returns tuples of key value pairs
            if (s[i], s[i+1]) not in parentheses.items():
                return False
            '''SOLUTION 3'''
            if s[i] in parentheses.keys():
                if parentheses[s[i]] not in s:
                    return False
        # if all characters are checked and pass test, return true
        return True
    '''
    *example*
    input: "()[]{}"
    iteration 1:
        i = 0
        s[i+1] = s[1] = ')'
        parentheses[s[0]] = ')'
        true, continue
    iteration 2
        i = 2
        s[i+1] = s[3] = ']'
        s[1] = ), parentheses[s[1]] = 
        
    '''
    ################SOLUTION THAT WORKS FOR ALL CASES#######################
    def isValid2(self, s):
        parentheses = {'(':')', '{':'}','[':']'}
        # instantiate empty list
        stack = []
        # iterate through characters in the string
        for char in s:
            # if the character is in the dictionary keys (aka a left bracket) append it to the list
            if char in parentheses.keys():  # 1
                stack.append(char)
            # else check if the list is empty (meaning it is the right bracket since those are not added to list)
            # OR (([]))[
            # if the value of the charcacter in the list is not the matching right bracket
            # this will also remove the charcter from the list and start fresh for the next iteration
            # return false
            elif len(stack) == 0 or parentheses[stack.pop()] != char:  # 2
                return False
        # if all conditions are met and there are no characters left in the stack (meaning there were matches found for each bracket)
        # this statement will return true
        return len(stack) == 0 # 3
     


if __name__ == '__main__':
    test_obj = Solution()
    test_method = test_obj.isValid2("()[]{}")
    print(test_method)
