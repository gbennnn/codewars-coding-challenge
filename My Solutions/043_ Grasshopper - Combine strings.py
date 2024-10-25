"""
Codewars Coding Challenge

Grasshopper - Combine strings

Combine strings function
Create a function named (combine_names) that accepts two parameters (first and last name). The function should return the full name.

Example:

combine_names('James', 'Stevens')
returns:

'James Stevens'

https://www.codewars.com/kata/55f73f66d160f1f1db000059/train/python
"""


# My Solution
def combine_names(fname, lname):
    return fname + " " + lname

"""
Sample Tests

import codewars_test as test
from solution import combine_names

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(combine_names("James", "Stevens"), "James Stevens")
        test.assert_equals(combine_names("Davy", "Back"), "Davy Back")
        test.assert_equals(combine_names("Arthur", "Dent"), "Arthur Dent")

"""