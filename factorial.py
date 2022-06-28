'''
Create a function that returns a factorial of any number
'''

'''

EXAMPLE:
input: 3
output: 6
'''

def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


print(factorial(8))