"""
Codewars Coding Challenge

Day 71/366

Level 7kyu

Naughty Or Nice

Santa is coming to town and he needs your help finding out who's been naughty or nice. You will be given an entire year of JSON data following this format:

{
    January: {
        '1': 'Naughty','2': 'Naughty', ..., '31': 'Nice'
    },
    February: {
        '1': 'Nice','2': 'Naughty', ..., '28': 'Nice'
    },
    ...
    December: {
        '1': 'Nice','2': 'Nice', ..., '31': 'Naughty'
    }
}
Your function should return "Naughty!" or "Nice!" depending on the total number of occurrences in a given year (whichever one is greater). If both are equal, return "Nice!"

def naughty_or_nice(data):
    pass


https://www.codewars.com/kata/5662b14e0a1fb8320a00005c/train/python

"""


# My Solution
def naughty_or_nice(data):
    total_naughty = 0
    total_nice = 0
    
    # Loop melalui setiap bulan
    for month in data.values():
        # Loop melalui setiap hari dalam bulan
        for day, status in month.items():
            if status == 'Naughty':
                total_naughty += 1
            elif status == 'Nice':
                total_nice += 1
    
    # Bandingkan total Naughty dan Nice
    if total_naughty > total_nice:
        return 'Naughty!'
    elif total_nice > total_naughty:
        return 'Nice!'
    else:
        return 'Nice!'

# Contoh penggunaan
data = {
    'January': {'1': 'Naughty', '2': 'Naughty', '31': 'Nice'},
    'February': {'1': 'Nice', '2': 'Naughty', '28': 'Nice'},
    'December': {'1': 'Nice', '2': 'Nice', '31': 'Naughty'}
}

print(naughty_or_nice(data))  # Output: Naughty!


"""
Solutions From Codewars

=1=
def naughty_or_nice(data):
    nice = 0
    for month in data:
        for day in data[month]:
            nice += 1 if data[month][day] == "Nice" else -1
    return "Nice!" if nice >= 0 else "Naughty!"


=2=
def naughty_or_nice(data):
    s = str(data)
    return 'Nice!' if s.count('Nice') >= s.count('Naughty') else 'Naughty!'


=3=
def naughty_or_nice(data):
    return 'Nice!' if str(data).count('Nice') >= str(data).count('Naughty') else 'Naughty!'


"""