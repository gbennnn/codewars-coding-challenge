"""
Codewars Coding Challenge

Day 66/366

Level 7kyu

The alphabet product

I have four positive integers, A, B, C and D, where A < B < C < D. The input is a list of the integers A, B, C, D, AxB, BxC, CxD, DxA in some order. Your task is to return the value of D.


def alphabet(ns):
    return #Good luck!


https://www.codewars.com/kata/63b06ea0c9e1ce000f1e2407/train/python

"""

# My Solution
def alphabet(ns):
    ns.sort()
    ns.remove(ns[0] * ns[1])
        
    return ns[-1] // ns[2]

print(alphabet([2, 3, 4, 1, 12, 6, 2, 4]))
print(alphabet([2, 6, 7, 3, 14, 35, 15, 5]))
print(alphabet([20, 10, 6, 5, 4, 3, 2, 12]))
print(alphabet([2, 6, 18, 3, 6, 7, 42, 14]))
print(alphabet([7, 96, 8, 240, 12, 140, 20, 56]))
print(alphabet([20, 30, 6, 7, 4, 42, 28, 5]))




"""
Sample Tests

import codewars_test as test
from solution import alphabet

@test.describe('Fixed Tests')
def tests():
    
    @test.it('Basic tests (d < 21)')
    def basic():
        test.assert_equals(alphabet([2, 3, 4, 1, 12, 6, 2, 4]), 4)
        test.assert_equals(alphabet([2, 6, 7, 3, 14, 35, 15, 5]), 7)
        test.assert_equals(alphabet([20, 10, 6, 5, 4, 3, 2, 12]), 5)
        test.assert_equals(alphabet([2, 6, 18, 3, 6, 7, 42, 14]), 7)
        test.assert_equals(alphabet([7, 96, 8, 240, 12, 140, 20, 56]), 20)
        test.assert_equals(alphabet([20, 30, 6, 7, 4, 42, 28, 5]), 7)
"""


"""
Solutions From Codewars

=1=
def alphabet(ns):
    a, b, c1, c2, _, _, _, cd = sorted(ns)
    return cd / c2 if a * b == c1 else cd / c1



=2=
def alphabet(ns):
    ns = sorted(ns)
    ns.remove(ns[0] * ns[1])
    return ns[-1] / ns[2]

"""