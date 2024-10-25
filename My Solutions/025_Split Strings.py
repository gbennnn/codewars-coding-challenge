"""
Codewars Coding Challenge

Split Strings

DESCRIPTION:
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']

https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python
"""

# My Solution
def solution(s):
    pairs = []
    for i in range(0, len(s), 2):
        pair = s[i:i+2]
        if len(pair) < 2:
            pair += "_"
        pairs.append(pair)
    return pairs

print(solution("abcdefg"))
print(solution("abcdef"))
        



"""
Sample Test
import codewars_test as test
from solution import *

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        tests = (
            ("asdfadsf", ['as', 'df', 'ad', 'sf']),
            ("asdfads", ['as', 'df', 'ad', 's_']),
            ("", []),
            ("x", ["x_"]),
        )

        for inp, exp in tests:
            test.assert_equals(solution(inp), exp)

"""


"""
Perfect Solution From Codewars


"""