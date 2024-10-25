"""
Codewars Coding Challenge

Day 47/366

Level : 8kyu

Sentence Smash

Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

Example
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

def smash(words):
    return ""

https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/python

"""


# My Solution
def smash(words):
    str_words = ""
    for i in range(len(words)):
        str_words += words[i] + " "
    return str_words.rstrip()

print(smash(["Hello", "World"]))



"""
Sample Tests

import codewars_test as test
from solution import smash

@test.describe("smash")
def _():
    @test.it("Should return empty string for empty array.")
    def _():
        test.assert_equals(smash([]), "")
        
    @test.it("One word example should return the word.")
    def _():
        test.assert_equals(smash(["hello"]), "hello")
        
    @test.it("Multiple words should be separated by spaces.")
    def _():
        test.assert_equals(smash(["hello", "world"]), "hello world")
        test.assert_equals(smash(["hello", "amazing", "world"]), "hello amazing world")
        test.assert_equals(smash(["this", "is", "a", "really", "long", "sentence"]), "this is a really long sentence")

"""


"""
Perfect Solutions From Codewars

=1=
def smash(words):
    return " ".join(words)

=2=
smash = ' '.join
"""
