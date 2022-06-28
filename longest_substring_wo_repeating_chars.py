'''
Given a string s, find the length of the longest substring without repeating characters.
'''
'''
EXAMPLE:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         # iterate over each character and add into new array
#         # check if the character is already in the array (unique)
#         # if it is not, add to array, else continue iterating
#         unique_char = []
#         for char in s:
#             print(char)
#             if char not in unique_char:
#                 unique_char.append(char)
                
#         print(unique_char)
#         return len(unique_char)
# DOESNT WORK because you have to return SUBSTRING, not subsequence

        start = maxLength = 0
        char_dict = {}
        
        # iterate over characters in string by index
        for i in range(len(s)):
            # check if the character is in the usedchar dict
            # check if start is less than 
            print(s[i])
            print(start)
            if s[i] in char_dict and start <= char_dict[s[i]]:
                
                start = char_dict[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            char_dict[s[i]] = i

        return maxLength
        