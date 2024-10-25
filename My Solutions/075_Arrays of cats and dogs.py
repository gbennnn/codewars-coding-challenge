"""
Codewars Coding Challenge

Day 75/366

Level 6kyu

Arrays of cats and dogs

Consider an array containing cats and dogs. Each dog can catch only one cat, but cannot catch a cat that is more than n elements away. Your task will be to return the maximum number of cats that can be caught.

For example:

solve(['D','C','C','D','C'], 2) = 2, because the dog at index 0 (D0) catches C1 and D3 catches C4. 
solve(['C','C','D','D','C','D'], 2) = 3, because D2 catches C0, D3 catches C1 and D5 catches C4.
solve(['C','C','D','D','C','D'], 1) = 2, because D2 catches C1, D3 catches C4. C0 cannot be caught because n == 1.
solve(['D','C','D','D','C'], 1) = 2, too many dogs, so all cats get caught!
Do not modify the input array.

More examples in the test cases. Good luck!


def solve(arr,n):
    pass


https://www.codewars.com/kata/5a5f48f2880385daac00006c/train/python

"""

# My Solution
# def solve(arr, n):
#     cats = [i for i, animal in enumerate(arr) if animal == 'C']
#     dogs = [i for i, animal in enumerate(arr) if animal == 'D']

#     max_cats_caught = 0

#     for dog in dogs:
#         for cat in cats:
#             if abs(dog - cat) <= n:
#                 max_cats_caught += 1
#                 cats.remove(cat)
#                 break

#     return max_cats_caught

def solve(arr, n):
    cats = [i for i, animal in enumerate(arr) if animal == "C"]
    dogs = [i for i, animal in enumerate(arr) if animal == "D"]
    
    max_cats_caught = 0
    
    for dog in dogs:
        for cat in cats:
            if abs(dog - cat) <= n:
                max_cats_caught += 1
                cats.remove(cat)
                break
    return max_cats_caught


# Test cases
print(solve(['D','C','C','D','C'], 2))  # Output: 2
print(solve(['C','C','D','D','C','D'], 2))  # Output: 3
print(solve(['C','C','D','D','C','D'], 1))  # Output: 2
print(solve(['D','C','D','D','C'], 1))  # Output: 2

"""
Sample Tests

test.it("Basic tests")
test.assert_equals(solve(['D','C','C','D','C'], 1),2)
test.assert_equals(solve(['C','C','D','D','C','D'],2),3)
test.assert_equals(solve(['C','C','D','D','C','D'],1),2)
test.assert_equals(solve(['D','C','D','C','C','D'],3),3)
test.assert_equals(solve(['C','C','C','D','D'],3),2)
test.assert_equals(solve(['C','C','C','D','D'],2),2)
test.assert_equals(solve(['C','C','C','D','D'],1),1)

"""


"""
Solutions From Codewars

=1=
def solve(arr, reach):
    dogs, nCats = {i for i,x in enumerate(arr) if x=='D'}, 0
    for i,c in enumerate(arr):
        if c == 'C':
            catchingDog = next((i+id for id in range(-reach,reach+1) if i+id in dogs), None)
            if catchingDog is not None:
                nCats += 1
                dogs.remove(catchingDog)
    return nCats


=2=
def solve(arr, n):
    arr = arr[:]
    count = 0
    for i, j in enumerate(arr):
        if j == 'D':
            for k in range(max(i - n, 0), min(i + n, len(arr) - 1) + 1):
                if arr[k] == 'C':
                    arr[k] = ''
                    count += 1
                    break
    return count


=3=
def solve(arr, n):
    count = 0
    for i in range(len(arr)):
        if arr[i] == 'D':
            for j in range(i-n, i+n+1):
                if 0 <= j < len(arr):
                    if arr[j] == 'C':
                        count += 1
                        arr[j] = 'c'
                        break
    return count

"""