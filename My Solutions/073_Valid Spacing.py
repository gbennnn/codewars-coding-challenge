""""
Codewars Coding Challenge

Day 73/366

Level 7kyu

Valid Spacing

Your task is to write a function called valid_spacing() or validSpacing() which checks if a string has valid spacing. The function should return either true or false (or the corresponding value in each language).

For this kata, the definition of valid spacing is one space between words, and no leading or trailing spaces. Words can be any consecutive sequence of non space characters. Below are some examples of what the function should return:

* 'Hello world'   => true
* ' Hello world'  => false
* 'Hello world  ' => false
* 'Hello  world'  => false
* 'Hello'         => true

Even though there are no spaces, it is still valid because none are needed:
* 'Helloworld'    => true
* 'Helloworld '   => false
* ' '             => false
* ''              => true
Note - there will be no punctuation or digits in the input string, only letters.


def valid_spacing(s):
    # write your code here
    pass


https://www.codewars.com/kata/5f77d62851f6bc0033616bd8/train/python

"""


# My Solution
def valid_spacing(s):
    if s.startswith(" ") or s.endswith(" "):
        return False
    if "  " in s:
        return False
    return True


# Test
print(valid_spacing("Hello world"))
print(valid_spacing(" Hello world"))


"""
Sample Tests

@test.describe('Sample Tests')
def sample():
    test.assert_equals(valid_spacing('Hello world'),True)
    test.assert_equals(valid_spacing(' Hello world'),False)
    test.assert_equals(valid_spacing('Hello  world '),False)
    test.assert_equals(valid_spacing('Hello'),True)
    test.assert_equals(valid_spacing('Helloworld'),True)
"""


"""
Solutions From Codewars

=1=
def valid_spacing(s):
    return s == ' '.join(s.split())


=2=
def valid_spacing(s):
    return s == s.strip() and '  ' not in s
"""