"""
Codewars Coding Challenge

Return the day

Complete the function which returns the weekday according to the input number:

1 returns "Sunday"
2 returns "Monday"
3 returns "Tuesday"
4 returns "Wednesday"
5 returns "Thursday"
6 returns "Friday"
7 returns "Saturday"
Otherwise returns "Wrong, please enter a number between 1 and 7"

https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/python
"""


# My Solution
def whatday(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if num >= 1 and num <= 7:
        return days[num - 1]
    else:
        return "Wrong, please enter a number between 1 and 7"

# print(whatday(0))
# print(whatday(1))
# print(whatday(2))
# print(whatday(3))
# print(whatday(4))
# print(whatday(5))
# print(whatday(6))
# print(whatday(7))
# print(whatday(8))





"""
Sample Tests


import codewars_test as test
from solution import whatday

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(whatday(1), 'Sunday')
        test.assert_equals(whatday(2), 'Monday')
        test.assert_equals(whatday(3), 'Tuesday')
        test.assert_equals(whatday(8), 'Wrong, please enter a number between 1 and 7')
        test.assert_equals(whatday(20), 'Wrong, please enter a number between 1 and 7')

"""



"""
Perfect Solution From Codewars


=1=
def whatday(num):
    return {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}.get(num, "Wrong, please enter a number between 1 and 7")


"""