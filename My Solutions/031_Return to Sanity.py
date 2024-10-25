"""
Codewars Coding Challenge

Return to Sanity

This function should return an object, but it's not doing what's intended. What's wrong?

def mystery():
    results = {
    'sanity': 'Hello'}
    return 
    results


https://www.codewars.com/kata/514a7ac1a33775cbb500001e/train/python
"""

# My Solution
def mystery():
    results = {
    'sanity': 'Hello'}
    return results


"""
Sample Test

import codewars_test as test
from solution import mystery

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        result=mystery()
        test.assert_equals(type(result), dict, "Mystery did not the right kind of object")
        test.assert_equals(result["sanity"], 'Hello', 'Mystery has not returned to sanity')

"""