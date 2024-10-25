"""
Codewars Coding Challenge

Binary Addition

Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)


https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python
"""


# My Solution
def add_binary(a,b):
    return bin(a + b)[2:]


# Sample test
"""
import codewars_test as test
from solution import add_binary

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(add_binary(1,1),"10")
        test.assert_equals(add_binary(0,1),"1")
        test.assert_equals(add_binary(1,0),"1")
        test.assert_equals(add_binary(2,2),"100")
        test.assert_equals(add_binary(51,12),"111111")
"""





"""
PERFECT SOLUTION FROM CODEWARS

=1=
def add_binary(a,b):
    return '{:b}'.format(a+b)


=2=
add_binary=lambda a,b: bin(a+b)[2:]


=3=
def add_binary(a,b):
    
    s = ""
    num = a + b
    
    while num > 0:
        s = str(num%2) + s
        num = num/2
        
    return s


=4=
def add_binary(a,b):
    return str(bin(a+b)).split('b')[1]


=5=
def add_binary(a,b):
    return '{number:b}'.format(number=a + b)
"""