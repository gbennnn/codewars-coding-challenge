"""
Codewars Coding Challenge

Day 61/366

Level 7kyu

Is every value in the array an array?

Is every value in the array an array?

This should only test the second array dimension of the array. The values of the nested arrays don't have to be arrays.

Examples:

[[1],[2]] => true
['1','2'] => false
[{1:1},{2:2}] => false

def arr_check(arr):
    return True


https://www.codewars.com/kata/582c81d982a0a65424000201/train/python

"""


# My Solutions
def arr_check(arr):
    for i in arr:
        if not isinstance(i, list):
            return False
    return True

# Test
print(arr_check([[1], [2]]))
print(arr_check(['1', '2']))


"""
Sample Tests

import codewars_test as test
from solution import arr_check

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(arr_check([]), True)
        test.assert_equals(arr_check([['string']]), True)
        test.assert_equals(arr_check([[], {}]), False)
        test.assert_equals(arr_check([[1], [2], [3]]), True)
        test.assert_equals(arr_check(["A", "R", "R", "A", "Y"]), False)

"""



"""
Solutions From Codewars

=1=
def arr_check(arr):
    return all(type(i) == list for i in arr)


"""