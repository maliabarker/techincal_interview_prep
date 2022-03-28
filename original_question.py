"""
IDEAS
given a hex code or rgb value, convert it to the other (hex code to rgb or rgb to hex code)
protons, neutrons, electrons in given element
given a force vector equation and displacement, find the work done
"""

# HEX TO DECIMAL
'''
   HEX    ||   DECIMAL  ||  CALCULATIONS       HEX    ||   DECIMAL  ||  CALCULATIONS
(base 16)     (base 10)
    A	        10                              1A	        26	      1*16^1 + 10*16^0 = 26
    B	        11                              1B	        27	      1*16^1 + 11*16^0 = 27
    C	        12                              1C	        28	      1*16^1 + 12*16^0 = 28
    D	        13                              1D	        29	      1*16^1 + 13*16^0 = 29
    E	        14                              1E	        30	      1*16^1 + 14*16^0 = 30
    F	        15                              1F	        31	      1*16^1 + 15*16^0 = 31

    A0	        160	    10*16^1 + 0*16^0 = 160
    B0	        176	    11*16^1 + 0*16^0 = 176
    C0	        192	    12*16^1 + 0*16^0 = 192
    D0	        208	    13*16^1 + 0*16^0 = 208
    E0	        224	    14*16^1 + 0*16^0 = 224
    F0	        240	    15*16^1 + 0*16^0 = 240

    0	        0
    1	        1
    2	        2
    3	        3
    4	        4
    5	        5
    6	        6
    7	        7
    8	        8
    9	        9
'''

"""
given hex code
instantiate dict with numerical values for each alphabetic key
iterate over code by two characters
convert each pair of characters to a decimal
for the first two (which represent red) assign the decimal to r
for the middle two (which represent green) assign the decimal to g
for the last two (which represent blue) assign the decimal to b
return a tuple the contains r,g,b respectively
"""

'''
INPUT : six character string
OUTPUT : tuple with three values coinciding to r, g, and b respectively
* example *
# input : FF0000
# output : (255,0,0)
'''


class Solution(object):
    def hex_to_rgb(self, hex_code):
        # instantiate dict to hold values of each character
        char_to_int = {
            'A' : 10,
            'B' : 11,
            'C' : 12,
            'D' : 13,
            'E' : 14,
            'F' : 15,
            '0'	: 0,
            '1'	: 1,
            '2'	: 2,
            '3'	: 3,
            '4'	: 4,
            '5'	: 5,
            '6'	: 6,
            '7'	: 7,
            '8'	: 8,
            '9'	: 9
        }

        # initialize i at zero
        i = 0
        # iterate through hex code in pairs of 2
        for i in range(0, len(hex_code), 2):
            # get value from dict and mupltiply by 16 if first character, 1 if second character
            first_num = (char_to_int[hex_code[i]])*16
            second_num = char_to_int[hex_code[i+1]]
            if i == 0:
                # if i = 0 meaning its the first pair, assign decimal to r
                r = first_num + second_num
            if i == 2:
                # if i = 2 meaning its the middle pair, assign decimal to g
                g = first_num + second_num
            if i == 4:
                # if i = 4 meaning its the last pair, assign decimal to b
                b = first_num + second_num
        # return f string of rgb value
        return print(f'rgb = {r, g, b}')


if __name__ == '__main__':
    test_obj = Solution()
    test_obj.hex_to_rgb('DA70D6')
