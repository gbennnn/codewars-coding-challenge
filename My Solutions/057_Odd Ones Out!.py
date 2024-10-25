"""
Codewars Coding Challenge

Day 57/366

Leve 7kyu

Odd Ones Out!

The town sheriff dislikes odd numbers and wants all odd numbered families out of town! In town crowds can form and individuals are often mixed with other people and families. However you can distinguish the family they belong to by the number on the shirts they wear. As the sheriff's assistant it's your job to find all the odd numbered families and remove them from the town!

Challenge: You are given a list of numbers. The numbers each repeat a certain number of times. Remove all numbers that repeat an odd number of times while keeping everything else the same.

odd_ones_out([1, 2, 3, 1, 3, 3]) = [1, 1]
In the above example:

the number 1 appears twice
the number 2 appears once
the number 3 appears three times
2 and 3 both appear an odd number of times, so they are removed from the list. The final result is: [1,1]

Here are more examples:

odd_ones_out([1, 1, 2, 2, 3, 3, 3]) = [1, 1, 2, 2]
odd_ones_out([26, 23, 24, 17, 23, 24, 23, 26]) = [26, 24, 24, 26]
odd_ones_out([1, 2, 3]) = []
odd_ones_out([1]) = []
Are you up to the challenge?



def odd_ones_out(numbers):
    pass # Your code


https://www.codewars.com/kata/5d376cdc9bcee7001fcb84c0/train/python

"""


# My Solution
def odd_ones_out(numbers):
    count = {}
    for i in numbers:
        count[i] = count.get(i, 0) + 1
    result = [i for i in numbers if count[i] % 2 == 0]
    return result


# Test
print(odd_ones_out([1,1,2,2,3,3,3]))
print(odd_ones_out([1,2,3,1,3,3]))
print(odd_ones_out([75,68,75,47,68]))





"""
Sample Tests

import codewars_test as test
from solution import odd_ones_out

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(odd_ones_out([1,2,3,1,3,3]), [1,1])
        test.assert_equals(odd_ones_out([75, 68, 75, 47, 68]), [75, 68, 75, 68])
        test.assert_equals(odd_ones_out([42, 72, 32, 4, 94, 82, 67, 67]), [67, 67])
        test.assert_equals(odd_ones_out([100, 100, 5, 5, 100, 50, 68, 50, 68, 50, 68, 5, 100]), [100, 100, 100, 100])
        test.assert_equals(odd_ones_out([82, 86, 71, 58, 44, 79, 50, 44, 79, 67, 82, 82, 55, 50]), [44, 79, 50, 44, 79, 50])
"""



"""
Solutions From Codewars

=1=
def odd_ones_out(numbers):
    return [i for i in numbers if numbers.count(i) % 2 == 0]


=2=
def odd_ones_out( _n ):
    out = []
    for i in _n:
        if _n.count(i) % 2 == 0:
            out.append(i)
    return out;


"""