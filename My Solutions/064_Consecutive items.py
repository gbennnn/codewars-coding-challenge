"""
Codewars Coding Challenge

Day 64/366

Level 7kyu

Consecutive items

You are given a list of unique integers arr, and two integers a and b. Your task is to find out whether or not a and b appear consecutively in arr, and return a boolean value (True if a and b are consecutive, False otherwise).

It is guaranteed that a and b are both present in arr.

def consecutive(arr, a, b):
    # Do some magic


https://www.codewars.com/kata/5f6d533e1475f30001e47514/train/python

"""

# My Solution
def consecutive(arr, a, b):
    idx_a = arr.index(a)
    idx_b = arr.index(b)
    return abs(idx_a - idx_b) == 1

# Tests
print(consecutive([1, 3, 5, 7], 3, 7))
print(consecutive([1, 3, 5, 7], 3, 1))


"""
Sample Tests

import codewars_test as test

@test.describe("Simple tests")
def test_group_1():
    @test.it("Test 1")
    def test_1():
        test.assert_equals(consecutive([1, 3, 5, 7], 3, 7), False)
    @test.it("Test 2")
    def test_2():
        test.assert_equals(consecutive([1, 3, 5, 7], 3, 1), True)
    @test.it("Test 3")
    def test_3():
        test.assert_equals(consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4), True)
"""


"""
Solutions From Codewars

=1=
def consecutive(A, a, b):
    return abs(A.index(a)-A.index(b))==1

"""