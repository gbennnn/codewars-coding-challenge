/*
Codewars Coding Challenge

Quarter of the year

Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

Constraint:

1 <= month <= 12


int quarter_of(int month){
    return 0;
}

https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/train/cpp
*/

// #include <iostream>
// using namespace std;

// My Solution
int quarter_of(int month){
    return (month - 1) / 3 + 1;
}

// int main(){

//     cout << quarter_of(7) << endl;

//     return 0;
// }



/*
Sample Tests

Describe(Sample_tests) {
  It(Base_cases) {
    Assert::That(quarter_of(1), Equals(1));
    Assert::That(quarter_of(3), Equals(1));
    Assert::That(quarter_of(5), Equals(2));
    Assert::That(quarter_of(7), Equals(3));
    Assert::That(quarter_of(9), Equals(3));
    Assert::That(quarter_of(11), Equals(4));
  }  
};
*/


/*
Perfect Solution From Codewars

int quarter_of(int month){
  return (month + 2) / 3;
}
*/