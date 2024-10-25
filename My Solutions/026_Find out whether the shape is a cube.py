"""
Codewars Coding Challenge

Find out whether the shape is a cube

To find the volume (centimeters cubed) of a cuboid you use the formula:

volume = Length * Width * Height

But someone forgot to use proper record keeping, so we only have the volume, and the length of a single side!

It's up to you to find out whether the cuboid has equal sides (= is a cube).

Return true if the cuboid could have equal sides, return false otherwise.

Return false for invalid numbers too (e.g volume or side is less than or equal to 0).

Note: side will be an integer

https://www.codewars.com/kata/58d248c7012397a81800005c/train/python
"""

# My Solution
def cube_checker(volume, side):
    # Check for invalid inputs
    if volume <= 0 or side <= 0:
        return False
    
    # Calculate the side length based on the volume
    calculated_side = volume ** (1/3)
    
    # Check if the calculated side length is approximately equal to the given side length
    return abs(calculated_side - side) < 1e-9

print(cube_checker(27, 3))  # Output: True (27 could be a cube with side length 3)
print(cube_checker(64, 4))  # Output: False (64 is not a cube with side length 4)

        



"""
Sample Test

import codewars_test as test
from solution import cube_checker

@test.describe("Fixed Tests")
def fixed_tests():
    for ((v,s), exp) in [ ((-12,2), False),((8, 3),  False),((8, 2),  True),((-8,-2), False),
            ((27, 3), True),((1, 5),  False),((125, 5),True),((125,-5),False),
            ((0, 0), False), ((0, 12), False),((12, -1),False),((1, 1),  True) ] :
        @test.it("Testing: volume = %s, side = %s, Expecting: %s" % (v, s, exp))
        def basic_test_cases():
            test.assert_equals(cube_checker(v,s), exp)

"""


"""
Perfect Solution From Codewars

=1=
def cube_checker(volume, side):
    return 0 < volume == side**3


=2=
def cube_checker(volume, side):
    return side > 0 and side ** 3 == volume

=3=
cube_checker = lambda v, s: v == s**3 > 0


=4=
def cube_checker(v, s):
    return False if v < 1 and s < 1 else v/(s*s) == s
    



=5=
def cube_checker(volume, side):
    if (volume and side > 0) and side ** 3 == volume:
        return 1
    else:
        return 0
"""