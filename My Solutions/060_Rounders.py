"""
Codewars Coding Challenge

Day 60/366

Level 7kyu

Simple Fun #17: Rounders

Task
We want to turn the given integer into a number that has only one non-zero digit using a tail rounding approach. This means that at each step we take the last non 0 digit of the number and round it to 0 or to 10. If it's less than 5 we round it to 0 if it's larger than or equal to 5 we round it to 10 (rounding to 10 means increasing the next significant digit by 1). The process stops immediately once there is only one non-zero digit left.

Example
For value = 15, the output should be 20

For value = 1234, the output should be 1000.

1234 -> 1230 -> 1200 -> 1000.

For value = 1445, the output should be 2000.

1445 -> 1450 -> 1500 -> 2000.

Input/Output
[input] integer value

A positive integer.

Constraints: 1 ≤ value ≤ 108

[output] an integer
The rounded number.



def rounders(value):
    pass


https://www.codewars.com/kata/58846d50f54f021d90000012/train/python

"""

# My Solution
def rounders(value):
    position = 1
    while value >= 10:
        last_digit = value % 10
        if last_digit >= 5:
            value = (value // 10) + 1
        else:
            value = value // 10
        position *= 10
    return value * position




# Tests
print(rounders(15))    # Output: 20
print(rounders(1234))  # Output: 1000
print(rounders(1445))  # Output: 2000



"""
Sample Tests

import codewars_test as test
from solution import rounders

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals( rounders(15) , 20)
        test.assert_equals( rounders(1234) , 1000)
        test.assert_equals( rounders(1445) , 2000)
        test.assert_equals( rounders(14) , 10)
        test.assert_equals( rounders(99) , 100)
        test.assert_equals( rounders(10) , 10)
"""


"""
Solution From Codewars

=1=
def rounders(value):
    for i in range(1, len(str(value))):
        value = round(value/10**i+.01) * 10**i
    return value


=2=
def rounders(value):
    return round(value) if value < 10 else 10 * rounders(int(value/10 + 0.5))


=3=
def rounders(value):
    for r in range(1, len(str(value))):
        value = round(value+.1, -r)
    return int(value)
"""