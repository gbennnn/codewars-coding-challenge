"""
Codewars Coding Challenge

Switch it Up!

When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

If your language supports it, try using a switch statement.

https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/python
"""


# My Solution
def switch_it_up(number):
    name_num = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return name_num[number]

# def switch_it_up(number):
#     result = ""
#     arr_number = [0,1,2,3,4,5,6,7,8,9]
#     name_num = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
#     if number in arr_number:
#         result = name_num[number]
#     return result




# Sample test
"""
import codewars_test as test
from solution import switch_it_up

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(switch_it_up(0), "Zero")
        test.assert_equals(switch_it_up(9), "Nine")

"""





"""
PERFECT SOLUTION FROM CODEWARS

=1=
def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]
    



=2=
switch_it_up=lambda x:"Zero One Two Three Four Five Six Seven Eight Nine".split()[x]



"""