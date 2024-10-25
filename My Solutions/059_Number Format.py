"""
Codewars Coding Challenge

Day 59/366

Level 6kyu

Number Format

Format any integer provided into a string with "," (commas) in the correct places.

Example:

For n = 100000 the function should return '100,000';
For n = 5678545 the function should return '5,678,545';
for n = -420902 the function should return '-420,902'.


def number_format(n):
    pass


https://www.codewars.com/kata/565c4e1303a0a006d7000127/train/python


"""


# My Solutions
def number_format(n):
    return "{:,}".format(n)

# Tests
print(number_format(1000))
print(number_format(10000))
print(number_format(100000))
print(number_format(1000000))



"""
Sample Tests

import codewars_test as test
from solution import number_format

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(number_format(100000), "100,000")
        test.assert_equals(number_format(5678545), "5,678,545")
        test.assert_equals(number_format(-420902), "-420,902")
        test.assert_equals(number_format(-3), "-3")
        test.assert_equals(number_format(-1003), "-1,003")
"""
