'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, 
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four 
is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it 
making four. The same principle applies to the number nine, which is written as IX. There are six instances 
where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

'''
GIVEN : string of roman numerals
OUTPUT : integer value of the given roman numeral string

* example *
Input: s = "III"
Output: 3
'''

class Solution(object):
    def romanToInt(self, s):
        """
        —given—
        :type s: str

        —returned—
        :rtype: int
        """
        
        # Instantiate a numerical value to add or subtract to
        # This will also be the value that is returned
        num_val = 0
        
        # an assertion error if the string is too long
        assert 1 <= len(s) <= 15
        
        # Instantiate a dictionary that holds the values of each roman numeral
        # This will be referred to when we want to get a value of a numeral
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Iterate through each character in the string
        for i in range(len(s)):
            # checking that the character is a valid roman numeral
            assert s[i] in roman_values.keys()
            
            # Start with the last character in the string
            if i == len(s) - 1:
                num_val += roman_values[s[i]]

            # check if character value is less than the previous character
            # this char value = roman_values[str[i]]
            # last char value = roman_values[str[i + 1]]
            elif roman_values[s[i]] < roman_values[s[i + 1]]:
                num_val -= roman_values[s[i]]

            # if this char value is equal to the last or greater than the last, add
            else:
                num_val += roman_values[s[i]]
            
        # Return the final numerical value
        return num_val

if __name__ == '__main__':
    test_object = Solution()
    test_method = test_object.romanToInt('MCMXCIV')
    print(test_method)