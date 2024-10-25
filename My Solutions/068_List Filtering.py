"""
Codewars Coding Challenge

Day 68/366

Level 7kyu

List Filtering

In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]


def filter_list(l):
    'return a new list with the strings filtered out'


https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

"""


# My Solution
def filter_list(l):
    return [i for i in l if isinstance(i, int)]


# Tests
print(filter_list([1,2,'a','b'])) # == [1,2]
print(filter_list([1,'a','b',0,15])) # == [1,0,15]
print(filter_list([1,2,'aasf','1','123',123])) # == [1,2,123]



"""
Sample Tests

import codewars_test as test
from solution import filter_list

@test.describe('Sample tests')
def sample_tests():
    @test.it('should work for basic examples')
    def basic_examples():
        test.assert_equals(filter_list([1, 2, 'a', 'b']), [1, 2], 'For input [1, 2, "a", "b"]')
        test.assert_equals(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15], 'Fot input [1, "a", "b", 0, 15]')
        test.assert_equals(filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123], 'For input [1, 2, "aasf", "1", "123", 123]')
"""


"""
Solutions From Codewars

=1=


"""