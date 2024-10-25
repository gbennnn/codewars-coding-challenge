"""
Codewars Coding Challenge

Vowel Count

Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.

https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
"""


# My Solution
def get_count(sentence):
    vowel_count = 0
    vowels = "aiueo"
    
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count


# Sample test
"""
import codewars_test as test
from solution import get_count

@test.describe("Sample tests")
def sample_tests():
    
    @test.it("Should count all vowels")
    def all_vowels():
        test.assert_equals(get_count("aeiou"), 5, f"Incorrect answer for \"aeiou\"")
        
    @test.it("Should not count \"y\"")
    def only_y():
        test.assert_equals(get_count("y"), 0, f"Incorrect answer for \"y\"")        
        
    @test.it("Should return 0 when no vowels")
    def no_vowels():
        test.assert_equals(get_count("bcdfghjklmnpqrstvwxz y"), 0, f"Incorrect answer for \"bcdfghjklmnpqrstvwxz y\"")
        
    @test.it("Should return 0 for empty string")
    def no_vowels():
        test.assert_equals(get_count(""), 0, f"Incorrect answer for empty string")
        
    @test.it("Should return 5 for \"abracadabra\"")
    def test_abracadabra():    
        test.assert_equals(get_count("abracadabra"), 5, f"Incorrect answer for \"abracadabra\"")
"""





"""
PERFECT SOLUTION FROM CODEWARS

=1=
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")


=2=
def getCount(s):
    return sum(c in 'aeiou' for c in s)


=3=
def getCount(inputStr):
    return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])


=4=
def getCount(inputStr):
    return len([x for x in inputStr if x in 'aeoiu'])


=5=
getCount = lambda s: sum(s.count(i) for i in 'aeiou')
"""