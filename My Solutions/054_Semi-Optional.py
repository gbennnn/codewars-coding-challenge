"""
Codewars Coding Challenge

Day 54/366

Level: 8kyu

Semi-Optional

We have implemented a function wrap(value) that takes a value of arbitrary type and wraps it in a new JavaScript Object or Python Dict setting the 'value' key on the new Object or Dict to the passed-in value.

So, for example, if we execute the following code:

wrapper_obj = wrap("my_wrapped_string"); 
 # wrapper_obj should be  {"value":"my_wrapped_string"}
We would then expect the following statement to be true:

wrapper_obj["value"] == "my_wrapped_string"
Unfortunately, the code is not working as designed. Please fix the code so that it behaves as specified.

def wrap(value):
    return {value:value}

https://www.codewars.com/kata/521cd52e790405a74800032c/train/python

"""

# My Solution
def wrap(value):
    return {"value":value}

"""
Sample Tests

import codewars_test as test
from solution import wrap

@test.describe("example")
def test_group():
    @test.it("fixed_test")
    def test_case():
        res = wrap("my_test")
        test.assert_equals(res["value"], "my_test")
        test.assert_equals(wrap(343)["value"], 343)
        obj = {"test":"testy"}
        test.assert_equals(wrap(obj)["value"], obj)
        
"""