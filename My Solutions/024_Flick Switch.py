"""
Codewars Coding Challenge

Flick Switch

Create a function that always returns True/true for every item in a given list.
However, if an element is the word 'flick', switch to always returning the opposite boolean value.

Examples
['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]

Notes
"flick" will always be given in lowercase.
A list may contain multiple flicks.
Switch the boolean value on the same element as the flick itself.


https://www.codewars.com/kata/64fbfe2618692c2018ebbddb/train/python
"""


# My Solution
def flick_switch(lst):
    switch = True
    result = []
    
    for item in lst:
        if item == "flick":
            switch = not switch
        result.append(switch)
    return result



"""
Sample Test

import codewars_test as test
from solution import flick_switch

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(flick_switch(['codewars', 'flick', 'code', 'wars']), [True, False, False, False])
        test.assert_equals(flick_switch(['flick', 'chocolate', 'adventure', 'sunshine']), [False, False, False, False])
        test.assert_equals(flick_switch(['bicycle', 'jarmony', 'flick', 'sheep', 'flick']), [True, True, False, False, True])
        test.assert_equals(flick_switch(['bicycle']), [True])
        test.assert_equals(flick_switch(['john, smith, susan', 'flick']), [True, False])
        test.assert_equals(flick_switch(['flick', 'flick', 'flick', 'flick', 'flick']), [False, True, False, True, False])
        test.assert_equals(flick_switch([]), [])
"""



"""
Perfect Solution From Codewars


=1=
def flick_switch(lst):
    flick = True
    return [ (flick := flick ^ (v=='flick')) for v in lst]
    
    

=2=
def flick_switch(lst):
    r = True
    return [(r := not r if a == 'flick' else r) for a in lst]
    
    
    
=3=
flick_switch=lambda a,b=True:[b:=not b if item=='flick'else b for item in a]



=4=
def flick_switch(lst):
    v = True
    return [(v := v ^ (x == "flick")) for x in lst]
    


=5=
def flick_switch(lst):
    fl = True
    return [fl:=bool((fl + (x == 'flick')) % 2) for x in lst]

"""