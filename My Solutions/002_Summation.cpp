/*
Codewars coding challenge

Summation
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0. Your function only needs to return the result, what is shown between parentheses in the example below is how you reach that result and it's not part of it, see the sample tests.

example:
2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/cpp
*/


// My Solution
#include <iostream>
using namespace std;

int summation(int num){
  int result = 0;
  for(int i = 1; i <= num; i++){
    result += i;
  }
  return result;
}

// int main(){
//     int num;
//     cout << "Masukkan angka: ";
//     cin >> num;
//     cout << summation(num);

//     return 0;
// }
