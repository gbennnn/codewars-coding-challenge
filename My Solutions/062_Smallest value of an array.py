"""
Codewars Coding Challenge

Day 62/366

Level 7kyu

Smallest value of an array

Write a function that can return the smallest value of an array or the index of that value. The function's 2nd parameter will tell whether it should return the value or the index.

Assume the first parameter will always be an array filled with at least 1 number and no duplicates. Assume the second parameter will be a string holding one of two values: 'value' and 'index'.

min([1,2,3,4,5], 'value') // => 1
min([1,2,3,4,5], 'index') // => 0


def find_smallest(numbers, to_return):
    return 0


https://www.codewars.com/kata/544a54fd18b8e06d240005c0/train/python


"""


# My Solution
def find_smallest(numbers, to_return):
    if to_return == "value":
        return min(numbers)
    else:
        return numbers.index(min(numbers))

# Test
print(find_smallest([1,2,3,4], "value"))
print(find_smallest([4,3,5,2], "index"))

"""
Sample Tests

import codewars_test as test
from solution import find_smallest

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_smallest([5,4,3,2,1],"value"),1)
        test.assert_equals(find_smallest([5,4,3,2,1],"index"),4)
        test.assert_equals(find_smallest([ 8, 0, 9],"index"),1)
        test.assert_equals(find_smallest([ 8, 0, 9],"value"),0)
        test.assert_equals(find_smallest([ 1, 1, 0, 0, 1, 1],"value"),0)
        test.assert_equals(find_smallest([ 1, 1, 0, 0, 1, 1],"index"),2)
        test.assert_equals(find_smallest([0], 'value'), 0)
        test.assert_equals(find_smallest([0], 'index'), 0)
"""


"""
Solutions From Codewars

=1=
def find_smallest(numbers,to_return):
    return min(numbers) if to_return == 'value' else numbers.index(min(numbers))
"""

