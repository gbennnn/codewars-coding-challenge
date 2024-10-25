"""
Codewars Coding Challenge

Brainfuck generator

Convert text to brainfuck
You are tasked to writting a function to_brainfuck/toBrainfuck that converts a given string to brainfuck that would print the given string. For example if we were to call to_brainfuck("Hello World!") it might give us a result that is something like: "-[------->+<]>-.-[->+++++<]>++.+++++++..+++.[--->+<]>-----.---[->+++<]>.-[--->+<]>---.+++.------.--------.-[--->+<]>.", if we execute that code we would get "Hello World!" at the output.

https://www.codewars.com/kata/579e646353ba33cce2000093/train/python

"""


# My Solution
def ord_to_bf(num):
    result = ""
    if num > 0:
        result += num * "+"
    else: 
        result += "-"
    result += ".>"
    return result

def to_brainfuck(string):
    result = ""
    for char in string:
        result += ord_to_bf(ord(char))
    return result

# print(to_brainfuck("Hello World"))



# Sample test
"""
import codewars_test as test
from solution import to_brainfuck
from preloaded import brainfuck_interpreter

@test.describe("Sample Tests")
def sample_tests():
    @test.it("Fixed Tests")
    def test_case():
        test.assert_equals(brainfuck_interpreter(to_brainfuck("Hello World!")), "Hello World!")
        test.assert_equals(brainfuck_interpreter(to_brainfuck("Bye bye birdy")), "Bye bye birdy")

"""





"""
PERFECT SOLUTION FROM CODEWARS

=1=
to_brainfuck=lambda s:"".join("+"*ord(x)+".>"for x in s)



=2=
to_brainfuck = lambda s: ''.join('+' * ord(i) + '.[-]' for i in s)



=3=
def to_brainfuck(string):
    seq = [0] + [*map(ord, string)]
    return ''.join('-+'[a > 0] * abs(a) + '.' for a in (y-x for x,y in zip(seq, seq[1:])))



=4=
def to_brainfuck(string):
    o = [ord(i) for i in string]
    r = list(j-i for i, j in zip(o, o[1::]))
    res = ""
    for i in ([o[0]] + r):
        if i < 0:
            res += "-"*(-i) + "."
        else:
            res += "+"*i + "."
    return res
    
    

=5=
def to_brainfuck(s):
    return '.>'.join('+' * ord(c) for c in s) + '.'
"""