"""
Codewars Coding Challenge

Capitalization and Mutability

Your coworker was supposed to write a simple helper function to capitalize a string (that contains a single word) before they went on vacation.

Unfortunately, they have now left and the code they gave you doesn't work. Fix the helper function they wrote so that it works as intended (i.e. it must make the first character in the string upper case).

The string will always start with a letter and will never be empty.

Examples:

"hello" --> "Hello"
"Hello" --> "Hello" (the first letter was already capitalized)
"a"     --> "A"


def capitalize_word (word : str) -> str:
    word[0] = word[0].upper()
    return word

https://www.codewars.com/kata/595970246c9b8fa0a8000086/train/python

"""


# My Solution
def capitalize_word (word : str) -> str:
    return word[0].upper() + word[1:]



print(capitalize_word("hello world"))
"""
Sample Tests

import codewars_test as test

try:
    from solution import capitalizeWord as capitalize_word
except ImportError:
    from solution import capitalize_word

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(capitalize_word('word'), 'Word')
        test.assert_equals(capitalize_word('i'), 'I')
        test.assert_equals(capitalize_word('glasswear'), 'Glasswear')

"""



"""
Perfect Solutions From Codewars

=1=
def capitalizeWord(word):
    return word.capitalize()


=2=
def capitalizeWord(s):
    return s.title()
"""