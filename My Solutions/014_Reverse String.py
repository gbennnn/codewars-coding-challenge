"""
Codewars

> Kumite

Reverse String

https://www.codewars.com/kumite/65c37d573817126686ff7bd9?sel=65c37d573817126686ff7bd9
"""


# Cara 1
def reverse_string(string):
    return string[::-1]

str_input = str(input("Masukkan string: "))
print("String anda:", str_input)
print("Reverse string #1:", reverse_string(str_input))

# Cara 2
reverse = lambda str_input : str_input[::-1]
print("Reverse string #2:", reverse(str_input))
