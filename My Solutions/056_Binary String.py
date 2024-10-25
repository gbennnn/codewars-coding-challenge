"""
Codewars Coding Challenge

Day 56/366

Level 7kyu

Simple Fun #194: Binary String
You are given a binary string (a string consisting of only '1' and '0'). The only operation that can be performed on it is a Flip operation.

It flips any binary character ( '0' to '1' and vice versa) and all characters to the right of it.

For example, applying the Flip operation to the 4th character of string "1001010" produces the "1000101" string, since all characters from the 4th to the 7th are flipped.

Your task is to find the minimum number of flips required to convert the binary string to string consisting of all '0'.

Example
For s = "0101", the output should be 3.

It's possible to convert the string in three steps:

"0101" -> "0010"
   ^^^
"0010" -> "0001"
    ^^
"0001" -> "0000"
     ^
Input/Output
[input] string s
A binary string.

[output] an integer
The minimum number of flips required.

def bin_str(s):
    pass

https://www.codewars.com/kata/58c218efd8d3cad11c0000ef/train/python

"""


# My Solution
def bin_str(s):
    curr = '1'
    count = 0
    for char in s:
        if char == curr:
            count += 1
            curr = '0' if curr == '1' else '1'
    return count





"""
Sample Tests

import codewars_test as test
from solution import bin_str

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(bin_str("0101"),3)
        test.assert_equals(bin_str("10000"),2)
        test.assert_equals(bin_str("0000000000"),0)
        test.assert_equals(bin_str("1111111111"),1)
        test.assert_equals(bin_str("10101010101010"),14)
        test.assert_equals(bin_str("11111000011111"),3)
        test.assert_equals(bin_str("000001111100000"),2)
        test.assert_equals(bin_str("111000000000"),2)
        test.assert_equals(bin_str("00000000111111111"),1)
        test.assert_equals(bin_str("1010101011111111111111000000000"),10)
"""


"""
Solution From Codewars


=1=
def bin_str(s):
    return s.count("10") * 2 + (s[-1] == "1")


"""