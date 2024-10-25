"""
Codewars Coding Challenge 

Day 49/366

Level: 8kyu

Double Char

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
Good Luck!


def double_char(s):
    pass


https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python

"""


# My Solution
def double_char(s):
    res = ""
    for i in s:
        res += i * 2
    return res

print(double_char("Beno"))



"""
Sample Tests

import codewars_test as test
from solution import double_char

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(double_char("String"),"SSttrriinngg")
        test.assert_equals(double_char("Hello World"),"HHeelllloo  WWoorrlldd")
        test.assert_equals(double_char("1234!_ "),"11223344!!__  ")
"""