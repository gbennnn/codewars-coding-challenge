"""
Codewars Coding Challenge

Draw stairs

Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

For example n = 3 result in:

"I\n I\n  I"
or printed:

I
 I
  I
Another example, a 7-step stairs should be drawn like this:

I
 I
  I
   I
    I
     I
      I


def draw_stairs(n):
    pass

https://www.codewars.com/kata/5b4e779c578c6a898e0005c5/train/python
"""

# My Solution
def draw_stairs(n):
    stairs = ""
    for i in range(n):
        stairs += " " * i + "I\n"
    return stairs[:-1]

print(draw_stairs(10))


"""
Sample Tests

import codewars_test as test
from solution import draw_stairs


@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(draw_stairs(3), '''I\n I\n  I''')
        test.assert_equals(draw_stairs(5), '''I\n I\n  I\n   I\n    I''')
"""


"""
Perfect Solutions From Codewars

=1=
def draw_stairs(n):
    return '\n'.join(' '*i+'I' for i in range(n))


=2=
def draw_stairs(n):
    return '\n'.join('I'.rjust(i + 1) for i in range(n))

"""