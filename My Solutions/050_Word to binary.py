"""
Codewars Coding Challenge

Day 50/366

Level: 7kyu

Word to binary

Write a function that takes a string and returns an array containing binary numbers equivalent to the ASCII codes of the characters of the string. The binary strings should be eight digits long.

Example: 'man' should return [ '01101101', '01100001', '01101110' ]


def word_to_bin(word):
    # code away!!!
    return []



https://www.codewars.com/kata/59859f435f5d18ede7000050/train/python
"""


# My Solutions
def word_to_bin(word):
    bin_list = []
    for char in word:
        ascii_code = ord(char)
        bin_reps = bin(ascii_code)[2:].zfill(8)
        bin_list.append(bin_reps)
    return bin_list

print(word_to_bin("Ony"))


"""
Sample Tests

import codewars_test as test
from solution import word_to_bin

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        for word,exp in [ ('man', [ '01101101', '01100001', '01101110' ]),
            ('AB', ['01000001', '01000010']),
            ('wecking',[ '01110111', '01100101', '01100011', '01101011', '01101001', '01101110', '01100111' ] ),
            ('Ruby',[ '01010010', '01110101', '01100010', '01111001' ] ),
            ('Yosemite',[ '01011001', '01101111', '01110011', '01100101', '01101101', '01101001', '01110100', '01100101' ] ) ]:
            test.assert_equals( word_to_bin(word), exp )


"""


"""
Perfefct Solutions From Codewars

=1=
def word_to_bin(word):
    return ['{:08b}'.format(ord(c)) for c in word]


=2=
def word_to_bin(word):
    return [ f"{ord(c):08b}" for c in word ]
"""