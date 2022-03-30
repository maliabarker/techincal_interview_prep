'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

'''
INPUT: list of strings
OUTPUT: the longest prefix (set of starting letters) that all words in list have in common
*example*
input: ["flower","flow","flight"]
output: "fl"
'''

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        lcps = []
        i = 0
        for i in range(len(strs) - 1):
            # assign values for the first and second words to compare
            first_word = strs[i]
            second_word = strs[i+1]
            # instantiate a new string to hold to lcp between these two words
            new_lcp = ''
            # iterate through each letter in first word
            for i in range(len(first_word)):
                # if the letters at this index are in both words and it's still in the length of word two, 
                # append to new lcp
                if i <= len(second_word) - 1 and first_word[i] == second_word[i]:
                    new_lcp+=first_word[i]
            # append new lcp to the list of lcps
            lcps.append(new_lcp)
        # return the sortest lcp in the list of lcps
        return print(min(lcps, key=len))



if __name__ == '__main__':
    test_obj = Solution()
    test_method = test_obj.longestCommonPrefix(["dog","racecar","car"])