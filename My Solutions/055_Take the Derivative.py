"""
Codewars Coding Challenge

Day 55/366

Level: 8kyu

Take the Derivative

Your function should multiply the two numbers, and then subtract 1 from the exponent. Then, it has to return an expression (like 28x^7). "^1" should not be truncated when exponent = 2.

For example:

derive(7, 8)
In this case, the function should multiply 7 and 8, and then subtract 1 from 8. It should output "56x^7", the first number 56 being the product of the two numbers, and the second number being the exponent minus 1.

derive(7, 8) --> this should output "56x^7" 
derive(5, 9) --> this should output "45x^8" 
Notes:

The output of this function should be a string
The exponent will never be 1, and neither number will ever be 0


def derive(coefficient, exponent): 
    # your code here
    pass


https://www.codewars.com/kata/5963c18ecb97be020b0000a2/train/python

"""

# My Solution
def derive(coefficient, exponent): 
    return "{}x^{}".format(coefficient * exponent, exponent - 1)

print(derive(7, 8))



"""
Sample Tests

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(derive(7,8), "56x^7")
    test.assert_equals(derive(5,9), "45x^8")
    
"""