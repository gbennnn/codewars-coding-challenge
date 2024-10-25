"""
Codewars Coding Challenge

Remove the minimum

The museum of incredibly dull things
The museum of incredibly dull things wants to get rid of some exhibits. Miriam, the interior architect, comes up with a plan to remove the most boring exhibits. She gives them a rating, and then removes the one with the lowest rating.

However, just as she finished rating all exhibits, she's off to an important fair, so she asks you to write a program that tells her the ratings of the exhibits after removing the lowest one. Fair enough.

Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

Examples
* Input: [1,2,3,4,5], output = [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]


def remove_smallest(numbers):
    return []

https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python

"""


# My Solution
def remove_smallest(numbers):
    if not numbers:
        return []
    min_idx = numbers.index(min(numbers))
    return numbers[:min_idx] + numbers[min_idx + 1:]

# print(remove_smallest([1,2,3,4,2,5]))





"""
Sample Tests

import codewars_test as test
from solution import remove_smallest
from numpy.random import randint

def randlist():
    return list(randint(400, size=randint(1, 10)))

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
        test.assert_equals(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
        test.assert_equals(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
        test.assert_equals(remove_smallest([]), [], "Wrong result for []")
        
    @test.it("check for mutations to original list")    
    def _():
        a = randlist() # generates the list
        b = list(a) # makes a swallow copy
        remove_smallest(a) # uses the original list with the function
        test.assert_equals(a, b, "You've mutated input list  (expectation assertion is on value of input list, not output of method)") # test the list match

"""



"""
Perfect Solutions From Codewars

=1=
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a


=2=
def remove_smallest(numbers):
    return [n for i, n in enumerate(numbers) if i != numbers.index(min(numbers))]



=3=
def remove_smallest(n):
    return n[:n.index(min(n))] + n[n.index(min(n)) + 1:] if n != [] else []

"""