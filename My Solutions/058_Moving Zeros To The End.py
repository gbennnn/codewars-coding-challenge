"""
Codewars Coding Challenge

Day 58/366

Level 5kyu

Moving Zeros To The End

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    return lst

https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

"""



# My Solution
def move_zeros(lst):
    zeros = [num for num in lst if num == 0]
    non_zeros = [num for num in lst if num != 0]
    return non_zeros + zeros


# Tests
print(move_zeros([1, 0, 1, 2, 0, 1, 3]))





"""
Sample Tests

import codewars_test as test
from solution import move_zeros

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(move_zeros(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
        test.assert_equals(move_zeros(
            [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        test.assert_equals(move_zeros([0, 0]), [0, 0])
        test.assert_equals(move_zeros([0]), [0])
        test.assert_equals(move_zeros([]), [])
"""



"""
Solutions From Codewars

=1=
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))


=2=
def move_zeros(array):
    return [x for x in array if x] + [0]*array.count(0)


=3=
def move_zeros(a):
    a.sort(key=lambda v: v == 0)
    return a

"""





