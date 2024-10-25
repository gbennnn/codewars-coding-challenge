"""
Codewars Coding Challenge

Day 63/366

Level 7kyu

Array Array Array

You are given an initial 2-value array (x). You will use this to calculate a score.

If both values in (x) are numbers, the score is the sum of the two. If only one is a number, the score is that number. If neither is a number, return 'Void!'.

Once you have your score, you must return an array of arrays. Each sub array will be the same as (x) and the number of sub arrays should be equal to the score.

For example:

if (x) == ['a', 3] you should return [['a', 3], ['a', 3], ['a', 3]].



def explode(arr):  
    pass


https://www.codewars.com/kata/57eb936de1051801d500008a/train/python

"""


# My Solution
def explode(arr):  
    if isinstance(arr[0], (int, float)) and isinstance(arr[1], (int, float)):
        score = arr[0] + arr[1]
    elif isinstance(arr[0], (int, float)):
        score = arr[0]
    elif isinstance(arr[1], (int, float)):
        score = arr[1]
    else:
        return "Void!"
    result = [arr] * score
    return result



"""
Sample tests

import codewars_test as test
from solution import explode

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(explode([9, 3]), [[9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3]])
        test.assert_equals(explode(['a', 3]), [['a', 3], ['a', 3], ['a', 3]] ) 
        test.assert_equals(explode([6, 'c']), [[6, 'c'], [6, 'c'], [6, 'c'], [6, 'c'], [6, 'c'], [6, 'c']]) 
        test.assert_equals(explode(['a', 'b']), 'Void!') 
        test.assert_equals(explode([1, 0]), [[1,0]]) 
        test.assert_equals(explode(["a", 0]), [])

"""


"""
Solutions From Codewars

=1=
def explode(arr):  
    numbers = [n for n in arr if type(n) == int]
    return [arr] * sum(numbers) if numbers else "Void!"


"""