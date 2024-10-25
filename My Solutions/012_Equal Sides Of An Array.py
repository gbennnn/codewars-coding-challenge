"""
Codewars Coding Challenge

Equal Sides Of An Array

You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

For example:

Let's say you are given the array {1,2,3,4,3,2,1}:
Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}:
Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

Last one:
You are given the array {20,10,-80,10,10,15,35}
At index 0 the left side is {}
The right side is {10,-80,10,10,15,35}
They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
Index 0 is the place where the left side and right side are equal.

Note: Please remember that in most programming/scripting languages the index of an array starts at 0.

Input:
An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.

Output:
The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.

Note:
If you are given an array with multiple answers, return the lowest correct index.


https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python
"""


# My Solution
def find_even_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        total_sum -= arr[i]
        if left_sum == total_sum:
            return i
        left_sum += arr[i]
    
    return -1





"""
// Sample test
import codewars_test as test
from solution import find_even_index

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
        test.assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
        test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
        test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
        test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
        test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
        test.assert_equals(find_even_index(list(range(1,100))),-1)
        test.assert_equals(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
        test.assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
        test.assert_equals(find_even_index(list(range(-100,-1))),-1)
        test.assert_equals(find_even_index([8,8]),-1)
        test.assert_equals(find_even_index([8,0]),0)
        test.assert_equals(find_even_index([0,8]),1)
        test.assert_equals(find_even_index([7,3,-3]),0)
        test.assert_equals(find_even_index([8]),0)
        test.assert_equals(find_even_index([10,-10]),-1)
        test.assert_equals(find_even_index([-3,2,1,0]),3)
        test.assert_equals(find_even_index([-15,5,11,17,19,-17,20,-6,17,-17,19,16,-15,-6,20,17]),8)
"""




"""
PERFECT SOLUTION FROM CODEWARS

=1=
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

=2=
def find_even_index(arr):
    left, right = 0, sum(arr)
    for i, e in enumerate(arr):
        right -= e
        if left == right:
            return i
        left += e
    return -1


=3=
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[i:]) == sum(arr[:i+1]):
           return i
    return -1


=4=
def find_even_index(arr):
    r = [i for i in range(len(arr)) if sum(arr[0:i]) == sum(arr[i+1:])]
    return r[0] if r else -1


=5=
def find_even_index(arr):
  return next(iter(i for i, _ in enumerate(arr) if sum(arr[:i+1]) == sum(arr[i:])), -1)
"""