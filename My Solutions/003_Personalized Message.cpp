/*
Codewars coding challenge

Personalized Message
Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:
case	                    return
name equals owner	        'Hello boss'
otherwise	                'Hello guest'

https://www.codewars.com/kata/5772da22b89313a4d50012f7/train/cpp
*/

// My Solution
#include <string>

std::string greet(const std::string& name, const std::string& owner) {
    return (name == owner) ? "Hello boss" : "Hello guest";
}


// Sample test
// Describe(Fixed_tests) {
//   It(Basic_cases) {
//     Assert::That(greet("Daniel", "Daniel"), Equals("Hello boss"));
//     Assert::That(greet("Greg", "Daniel"), Equals("Hello guest"));
//   }
// };