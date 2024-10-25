/*
Codewars coding challenge

Even or Odd
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/cpp

*/

// My Solution 1
#include <string>

std::string even_or_odd_1(int number){
    if(number % 2 == 0)
        return "Even";
    else
        return "Odd";
}

// My Solution 2
std::string even_or_odd_2(int number){
    return (number % 2 == 0) ? "Even" : "Odd";
}