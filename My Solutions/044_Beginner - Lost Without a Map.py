"""
Codewars Coding Challenge

Beginner - Lost Without a Map

Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]

def maps(a):
    pass

https://www.codewars.com/kata/57f781872e3d8ca2a000007e/train/python
"""


# My Solution
def maps(arr):
    return [num * 2 for num in arr]

print(maps([1,2,3]))

"""
Sample Tests

import codewars_test as test
from solution import maps

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(maps([1, 2, 3]), [2, 4, 6])
        test.assert_equals(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
        test.assert_equals(maps([]), [])
"""