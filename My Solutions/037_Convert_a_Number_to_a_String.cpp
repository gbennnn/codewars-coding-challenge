/*
Codewars Coding Chellenge

Convert a Number to a String!

We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?

Examples (input --> output):
123  --> "123"
999  --> "999"
-100 --> "-100"


#include <string>

std::string number_to_string(int num) {
  // your code here
}


https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/cpp
*/

// My Solution
#include <string>
using namespace std;

string number_to_string(int num) {
    return to_string(num);
}



/*
Sample Tests

Describe(number_to_string_function) {
  It(should_convert_a_number_to_string) {
    Assert::That(number_to_string(1+2), Equals("3"));
    Assert::That(number_to_string(67), Equals("67"));
    Assert::That(number_to_string(-5), Equals("-5"));
  }
};


*/