"""
Codewars Coding Challenge

Sum without highest and lowest number

Task
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.

Example
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
Input validation
If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.


def sum_array(arr):
    #your code here

https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python
"""


# My Solution
def sum_array(arr):
    if not arr or len(arr) <= 1:
        return 0
    return sum(arr) - max(arr) - min(arr)

# print(sum_array([6, 2, 1, 8, 10]))


"""
Sample Tests

import codewars_test as test
from solution import sum_array

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('None or Empty')
    def basic_test_cases():
        test.assert_equals(sum_array(None), 0)
        test.assert_equals(sum_array([]), 0)

    @test.it("Only one Element")
    def one_test_cases():
        test.assert_equals(sum_array([3]), 0)
        test.assert_equals(sum_array([-3]), 0)
        
    @test.it("Only two Element")
    def two_test_cases():
        test.assert_equals(sum_array([ 3, 5]), 0)
        test.assert_equals(sum_array([-3, -5]), 0)

    @test.it("Real Tests")
    def real_test_cases():
        test.assert_equals(sum_array([6, 2, 1, 8, 10]), 16)
        test.assert_equals(sum_array([6, 0, 1, 10, 10]), 17)
        test.assert_equals(sum_array([-6, -20, -1, -10, -12]), -28)
        test.assert_equals(sum_array([-6, 20, -1, 10, -12]), 3)
"""


"""
Perfect Solution From Codewars

=1=
def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0


=2=
def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr else 0

=3=
def sum_array(arr):
    return sum(sorted(arr or [])[1:-1])


=4=
sum_array=lambda a:a and sum(sorted(a)[1:-1])or 0

=5=
def sum_array(arr):
if arr is None or len(arr) < 2:
    return 0

    mi, ma, s = arr[0], arr[0], 0

    for x in arr:
    if x > ma:
        ma = x
    elif x < mi:
        mi = x
    
    s += x
    
    return s - mi - ma

"""