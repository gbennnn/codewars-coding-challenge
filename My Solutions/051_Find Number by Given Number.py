"""
Codewars Coding Challenge

Day 51/366

Level: 8kyu

Find numbers which are divisible by given number

Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of numbers and the second is the divisor.

Example(Input1, Input2 --> Output)
[1, 2, 3, 4, 5, 6], 2 --> [2, 4, 6]


def divisible_by(numbers, divisor):


https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python

"""


# My Solution
def divisible_by(numbers, divisor):
    result = []
    for i in numbers:
        if i % divisor == 0:
            result.append(i)
    return result


print(divisible_by([1,2,3,4,5,6], 2))





"""
Sample tests

import codewars_test as test
from solution import divisible_by

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(divisible_by([1,2,3,4,5,6], 2), [2,4,6])
        test.assert_equals(divisible_by([1,2,3,4,5,6], 3), [3,6])
        test.assert_equals(divisible_by([0,1,2,3,4,5,6], 4), [0,4])
        test.assert_equals(divisible_by([0], 4), [0])
        test.assert_equals(divisible_by([1,3,5], 2), [])
        test.assert_equals(divisible_by([0,1,2,3,4,5,6,7,8,9,10], 1), [0,1,2,3,4,5,6,7,8,9,10])
"""

"""
Solutions From Codewars

=1=
def divisible_by(numbers, divisor):   
    return [num for num in numbers if num % divisor == 0]

"""