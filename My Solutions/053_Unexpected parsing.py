"""
Codewars Coding Challenge

Day 53/366

Level 8kyu

Unexpected parsing

Here is a piece of code:

def get_status(is_busy):
    status = "busy" if is_busy else "available"
    return status
Expected Behaviour
Function should return a dictionary/Object/Hash with "status" as a key, whose value can : "busy" or "available" depending on the truth value of the argument is_busy.

But as you will see after clicking RUN or ATTEMPT this code has several bugs, please fix them.


https://www.codewars.com/kata/54fdaa4a50f167b5c000005f/train/python

"""

# My Solution
def get_status(is_busy):
    status = "busy" if is_busy else "available"
    return {"status": status}

print(get_status(True))



"""
Sample Tests

import codewars_test as test
from solution import get_status

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(get_status(True)["status"], "busy")
        test.assert_equals(get_status(False)["status"], "available")
"""