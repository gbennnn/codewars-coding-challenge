"""
Codewars Coding Challenge

Day 67/366

Level 6kyu

N smallest elements in original order

Your task is to write a function that does just what the title suggests (so, fair warning, be aware that you are not getting out of it just throwing a lame bas sorting method there) with an array/list/vector of integers and the expected number n of smallest elements to return.

Also:

the number of elements to be returned cannot be higher than the array/list/vector length;
elements can be duplicated;
in case of duplicates, just return them according to the original order (see third example for more clarity).
Same examples and more in the test cases:

first_n_smallest([1,2,3,4,5],3) == [1,2,3]
first_n_smallest([5,4,3,2,1],3) == [3,2,1]
first_n_smallest([1,2,3,4,1],3) == [1,2,1]
first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
first_n_smallest([1,2,3,4,5],0) == []

Performance version by FArekkusu also available.


def first_n_smallest(arr, n):
    pass


https://www.codewars.com/kata/5aec1ed7de4c7f3517000079/train/python

"""


# My Solution
def first_n_smallest(arr, n):
    arr = sorted(enumerate(arr), key=lambda x: x[1])[:n]
    return [i[1] for i in sorted(arr, key=lambda x: x[0])]



"""
Sample Tests

import codewars_test as test
from solution import first_n_smallest

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(first_n_smallest([1,2,3,4,5],3), [1,2,3])
        test.assert_equals(first_n_smallest([5,4,3,2,1],3), [3,2,1])
        test.assert_equals(first_n_smallest([1,2,3,1,2],3), [1,2,1])
        test.assert_equals(first_n_smallest([1,2,3,-4,0],3), [1,-4,0])
        test.assert_equals(first_n_smallest([1,2,3,4,5],0), [])
        test.assert_equals(first_n_smallest([1,2,3,4,5],5), [1,2,3,4,5])
        test.assert_equals(first_n_smallest([1,2,3,4,2],4), [1,2,3,2])
        test.assert_equals(first_n_smallest([2,1,2,3,4,2],2), [2,1])
        test.assert_equals(first_n_smallest([2,1,2,3,4,2],3), [2,1,2])
        test.assert_equals(first_n_smallest([2,1,2,3,4,2],4), [2,1,2,2])
"""

"""
Solutions From Codewars

=1=
def first_n_smallest(arr, n):
    m = sorted(arr)[:n]
    return [m.pop(m.index(i)) for i in arr if i in m]


=2=
def first_n_smallest(l, n):
    a = sorted(l)[:n]
    m = []
    for i in l:
        if i in a:
            m.append(i)
            a.pop(a.index(i))
    return m

=3=
def first_n_smallest(arr, n):
    return [x[1] for x in sorted(sorted(enumerate(arr), key=lambda x: x[1])[:n])]
"""
