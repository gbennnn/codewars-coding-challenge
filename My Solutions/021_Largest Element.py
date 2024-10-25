"""
Codewars Coding Challenge

Largest Elements

Write a program that outputs the top n elements from a list.

Example:

largest(2, [7,6,5,4,3,2,1])
# => [6,7]

https://www.codewars.com/kata/53d32bea2f2a21f666000256/train/python
"""


# My Solution
def largest(n, arr):
    result = sorted(arr, reverse=True)[:n]
    return sorted(result, reverse=False)

# print(largest(2, [7,6,5,4,3,2,1]))




# Sample test
"""
import codewars_test as test
from solution import largest

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(largest(2, [10,9,8,7,6,5,4,3,2,1]), [9,10])
        test.assert_equals(largest(3, [5,1,5,2,3,1,2,3,5]), [5,5,5])
        test.assert_equals(largest(7, [9,1,50,22,3,13,2,63,5]), [3, 5, 9, 13, 22, 50, 63])

"""


"""
PERFECT SOLUTION FROM CODEWARS

=1=
def largest(n,xs):
  return (sorted(xs, reverse=True)[0:n])[::-1]


=2=
import heapq

def largest(n,xs):
  return sorted(heapq.nlargest(n, xs))


=3=
def largest(n,xs):
  return sorted(xs)[len(xs)-n:]
"""
