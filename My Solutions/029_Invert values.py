"""
Codewars Coding Challenge

Invert values

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers. Do not mutate the input array/list.


https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python
"""


# My Solution
def invert(lst):
    return [-x for x in lst]



"""
Sample Test

import codewars_test as test
from solution import invert

@test.describe("Invert values")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(invert([1,2,3,4,5]),[-1,-2,-3,-4,-5])
        test.assert_equals(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5])
        test.assert_equals(invert([]), [])
"""


"""
Perfect Solution From Codewars

=1=
def invert(lst):
    return [i*-1 for i in lst]



=2=
invert = lambda lst: [-e for e in lst]


"""