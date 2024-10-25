""""
Codewars Coding Challenge 

Day 70/366

Level 7kyu

Trilingual democracy

Switzerland has four official languages: German, French, Italian, and Romansh.1

When native speakers of one or more of these languages meet, they follow certain regulations to choose a language for the group.2 Here are the rules for groups of exactly three3 people:4

When all three are native speakers of the same language, it also becomes their group's language.5a

When two are native speakers of the same language, but the third person speaks a different language, all three will converse in the minority language.5b

When native speakers of three different languages meet, they eschew these three languages and instead use the remaining of the four official languages.5c

The languages are encoded by the letters D for Deutsch, F for Français, I for Italiano, and K for Rumantsch.6

Your task is to write a function that takes a list of three languages and returns the language the group should use.7 8

Examples:9

The language for a group of three native French speakers is French: FFF → F

A group of two native Italian speakers and a Romansh speaker converses in Romansh: IIK → K

When three people meet whose native languages are German, French, and Romansh, the group language is Italian: DFK → I

1 The first sentence of the description and the first sentence of this footnote are true. Almost all other sentences in the description and the footnotes are complete hogwash.

2 This footnote has no useful content. It was inserted solely to make the next footnote – at least in some sense – self-referential.

3 Thou shalt count to three, no more, no less. Four shalt thou not count, neither count thou two, excepting that thou then proceed to three. Five is right out.

4 These rules were carefully designed with a focus on practices that could be perceived as exclusive or discriminatory.

5a The first rule is based on pragmatics and aesthetics: choosing a language other than the one spoken by all three would introduce gratuitous friction and asymmetry.

5b The second rule is inspired by a strong sense of politeness and modesty: it would feel arrogant for the majority to impose its language upon the minority.

5c The third rule originates from a deep belief in fairness: picking one of the languages spoken in the group would arbitrarily privilege one member and disadvantage the two others.

6 The choice of the letter K for Rumantsch was an accident – during the linguistic rule standardization process in 1964 a typist at the Bundesamt für Organisation misread a hand-written R as K. Unfortunately, correcting this mistake would break backwards compatibility.

7 The input argument of your function will always be a string (or an array, depending on programming language) of exactly three upper-case characters from the set D, F, I and K, and the return value of your function must be a single upper-case character from this set.

8 This footnote is a deceptive non sequitur, as it erroneously claims that the multilingual people of Switzerland are united by a shared fondness for watchmaking, bit twiddling, the Basic Latin Unicode block, and Gruyère cheese.

9 This is footnote 9, and it's just as nonsensical as footnotes 2, 3, and 8, since it merely observes that 9 happens to be the bitwise exclusive-or of 2, 3, and 8.

https://www.codewars.com/kata/62f17be8356b63006a9899dc/train/python

"""

# My Solution
def trilingual_democracy(group):
    # Hitung jumlah masing-masing bahasa dalam kelompok
    count_D = group.count('D')
    count_F = group.count('F')
    count_I = group.count('I')
    count_K = group.count('K')
    
    # Aturan 5a: Jika semua tiga orang berbicara dalam bahasa yang sama
    if count_D == 3 or count_F == 3 or count_I == 3 or count_K == 3:
        return group[0]  # Mengembalikan salah satu bahasa yang ada di grup
    
    # Aturan 5b: Jika dua orang berbicara dalam bahasa yang sama dan yang ketiga berbicara bahasa yang berbeda
    if count_D == 2 and count_F == 1:
        return 'F'
    if count_D == 2 and count_I == 1:
        return 'I'
    if count_D == 2 and count_K == 1:
        return 'K'
    if count_F == 2 and count_D == 1:
        return 'D'
    if count_F == 2 and count_I == 1:
        return 'I'
    if count_F == 2 and count_K == 1:
        return 'K'
    if count_I == 2 and count_D == 1:
        return 'D'
    if count_I == 2 and count_F == 1:
        return 'F'
    if count_I == 2 and count_K == 1:
        return 'K'
    if count_K == 2 and count_D == 1:
        return 'D'
    if count_K == 2 and count_F == 1:
        return 'F'
    if count_K == 2 and count_I == 1:
        return 'I'
    
    # Aturan 5c: Jika tiga orang berbicara dalam bahasa yang berbeda
    return 'D' if count_D == 0 else 'F' if count_F == 0 else 'I' if count_I == 0 else 'K'

# Tests
print(trilingual_democracy('FFF'))  # Output: F
print(trilingual_democracy('IIK'))  # Output: K
print(trilingual_democracy('DFK'))  # Output: I



"""
Sample Tests

import codewars_test as test

from solution import trilingual_democracy

def do_test(group, want):
    test.assert_equals(trilingual_democracy(group), want, "for group '"+group+"'")

@test.it('Example tests')
def example_tests():
    do_test("FFF", "F")
    do_test("IIK", "K")
    do_test("DFK", "I")
"""


"""
Solutions From Codewars

=1=
def trilingual_democracy(group):
    return chr(ord(group[0])^ord(group[1])^ord(group[2]))


=2=
def trilingual_democracy(group):
    ols, inv = {"D":1, "F":2, "I":3, "K":4}, {1:"D", 2:"F", 3:"I", 4:"K"}
    res = ols[group[0]] ^ ols[group[1]] ^ ols[group[2]]
    return inv[res] if res in inv else (set("DFIK") - set(group)).pop()
"""