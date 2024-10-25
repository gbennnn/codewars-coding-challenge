"""
Codewars Coding Challenge

All Star Code Challenge #18

Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

("Hello", "o")  ==>  1
("Hello", "l")  ==>  2
("", "z")       ==>  0
str_count("Hello", 'o'); // returns 1
str_count("Hello", 'l'); // returns 2
str_count("", 'z'); // returns 0
Notes
The first argument can be an empty string
In languages with no distinct character data type, the second argument will be a string of length 1


https://www.codewars.com/kata/5865918c6b569962950002a1/train/python
"""


# My Solution
def str_count(strng, letter):
    return strng.count(letter)


# Sample test
"""
@test.describe('Should return the correct character count')
def fixed():
    @test.it("")
    def f():
        test.assert_equals(str_count('hello', 'l'), 2)
        test.assert_equals(str_count('hello', 'e'), 1)
        test.assert_equals(str_count('codewars', 'c'), 1)
        test.assert_equals(str_count('ggggg', 'g'), 5)
        test.assert_equals(str_count('hello world', 'o'), 2)
        test.assert_equals(str_count('', 'z'), 0)
"""





"""
PERFECT SOLUTION FROM CODEWARS

=1=
strCount = str.count


=2=
str_count = lambda strng, letter: strng.count(letter)

=3=
def str_count(strng, letter):
    score = 0
    for char in strng:
        if char == letter:
            score += 1
    return score 


=4=
def strCount(string, letter):
    return len([i for i in string if i == letter])


=5=
def str_count(strng, letter):
    return sum(1 for i in strng if i in letter)
"""