"""
Codewars Coding Challenge

Day 69/366

Level 7kyu

Thinkful - List and Loop Drills: Lists of lists

You have a two-dimensional list in the following format:

data = [[2, 5], [3, 4], [8, 7]]
Each sub-list contains two items, and each item in the sub-lists is an integer.

Write a function process_data()/processData() that processes each sub-list like so:

[2, 5] --> 2 - 5 --> -3
[3, 4] --> 3 - 4 --> -1
[8, 7] --> 8 - 7 --> 1
and then returns the product of all the processed sub-lists: -3 * -1 * 1 --> 3.

For input, you can trust that neither the main list nor the sublists will be empty.

def process_data(data):
    pass # Your code here



https://www.codewars.com/kata/586e1d458cb711f0a800033b/train/python

"""


# My Solution
def process_data(data):
    result = 1
    for sublist in data:
        diff = sublist[0] - sublist[1]
        result *= diff
    
    return result




"""
Sample Tests

from solution import process_data
import codewars_test as test

@test.describe("Lists of lists")
def lists_of_lists():
    
    @test.it("Examples")
    def examples():
        test.assert_equals(process_data([[2, 5], [3, 4], [8, 7]]), 3)
        test.assert_equals(process_data([[2, 9], [2, 4], [7, 5]]), 28)
"""



"""
Solutions From Codewars

=1=
from math import prod

def process_data(data):
    return prod(i[0] - i[1] for i in data)

"""