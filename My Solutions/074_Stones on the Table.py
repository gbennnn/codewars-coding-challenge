"""
Codewars Coding Challenge

Day 74/366

Level 7kyu

Stones on the Table

There are some stones on Bob's table in a row, and each of them can be red, green or blue, indicated by the characters R, G, and B.

Help Bob find the minimum number of stones he needs to remove from the table so that the stones in each pair of adjacent stones have different colors.

Examples:

"RGBRGBRGGB"   => 1
"RGGRGBBRGRR"  => 3
"RRRRGGGGBBBB" => 9


def solution(stones):
    # Do some magic


https://www.codewars.com/kata/5f70e4cce10f9e0001c8995a/train/python

"""


# My Solution
def solution(stones):
    count = 0
    for i in range(1, len(stones)):
        if stones[i] == stones[i - 1]:
            count += 1
    return count


# Test Cases
print(solution("RGBRGBRGGB"))   # Output: 1
print(solution("RGGRGBBRGRR"))  # Output: 3
print(solution("RRRRGGGGBBBB")) # Output: 9


"""
Solutions From Codewars

=1=
def solution(s):
    st=[1 for i in range(1,len(s)) if s[i-1]==s[i]]
    return sum(st)


=2=
def solution(s):
    return sum(i==j for i,j in zip(s,s[1:]))
"""