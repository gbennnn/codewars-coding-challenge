"""
Codewars Coding Challenge

Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!

https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python
"""


# My Solution
def find_missing_letter(chars):
    for i in range(1, len(chars)):
        if ord(chars[i]) - ord(chars[i - 1]) > 1:
            return chr(ord(chars[i - 1]) + 1)





"""
Sample test

import codewars_test as test
from solution import find_missing_letter

@test.describe("Kata Tests")
def kata_tests():
    
    @test.it("Sample Tests")
    def sample_tests():
        test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
        test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')
        test.assert_equals(find_missing_letter(['b','d']), 'c')


"""



"""
Perfect Solution From Codewaars

=1=
def find_missing_letter(c):
    return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))
    
    
    
=2=
def find_missing_letter(chars):
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 'w', 'x', 'y', 'z']
    indexes = []
    for char in chars:
        indexes.append(list1.index(char.lower()))
    i = 0
    final_index = 0
    for index in indexes:
        if(indexes[i]-indexes[i-1] > 1):
            final_index = indexes[i]-1
        i += 1
    for char in chars:
        if char.isupper():
            return list1[final_index].upper()
        else:
            return list1[final_index]




=3=
def find_missing_letter(chars):
    return chr(sum(range(ord(chars[0]), ord(chars[-1]) + 1)) - sum(map(ord, chars)))




=4=
find_missing_letter=lambda a,b=__import__('string').ascii_letters:next(filter(lambda e:e not in a,b[b.index(a[0]):]))



=5=
"""