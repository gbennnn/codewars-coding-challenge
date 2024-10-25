"""
Codewars Coding Challenge

Day 65/366

Level 6kyu

Consecutive count

I want to know the size of the longest consecutive elements of X in Y. You will receive two arguments: items and key. Return the length of the longest segment of consecutive keys in the given items.

Notes:

The items and the key will be either an integer or a string (consisting of letters only)
If the key does not appear in the items, return 0
Examples
90000, 0           -->  4
"abcdaaadse", "a"  -->  3
"abcdaaadse", "z"  -->  0


https://www.codewars.com/kata/59c3e819d751df54e9000098/train/python

"""

# My Solution
def get_consective_items(items, key): 
    long_run = 0
    curr_run = 0
    items_str = str(items)
    
    for char in items_str:
        if char == str(key):
            curr_run += 1
            long_run = max(long_run, curr_run)
        else:
            curr_run = 0
    return long_run
            

# Tests
print(get_consective_items(90000, 0)) # out: 4



"""
Sample Tests

import codewars_test as test
from solution import get_consective_items

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(get_consective_items(90000, 0), 4)
        test.assert_equals(get_consective_items('ascasdaiiiasdacasdiiiiicasdasdiiiiiiiiiiisdasdasdiii', 'i'), 11)
"""


"""
Solutions From Codewars

=1=


"""