/*
Codewars Coding Challenge

Day 77/366

Level 6kyu

Valid Braces

Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False

bool valid_braces(std::string braces) 
{
  // valid or not valid?
}


https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/cpp

*/


// My Solution
#include <iostream>
#include <stack>
#include <string>

bool valid_braces(std::string braces) {
    std::stack<char> braceStack;

    for(char c : braces){
        if (c == '(' || c == '{' || c == '['){
            braceStack.push(c);
        }else if(c == ')' || c == '}' || c == ']'){
            if (braceStack.empty()){
                return false; // kurung tutup tanpa pasangan
            }else{
                char top = braceStack.top();
                braceStack.pop();
                // cocokan kurung buka dengan kurung tutup
                if((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')){
                        return false; // kurung tdkk seimbang
                    }
            }
        }
    }

    return braceStack.empty(); // return true jika semua kurung memiliki pasangan
}

// Test Cases
int main(){
    std::cout << valid_braces("(){}[]") << std::endl;
    std::cout << valid_braces("([{}])") << std::endl;
    std::cout << valid_braces("(}") << std::endl;
    std::cout << valid_braces("[(])") << std::endl;
    std::cout << valid_braces("[({})](]") << std::endl;
}


/*
Codewars Sample Tests

// Some macros for easy true/false assertions
#define assert_valid(s) \
  if(!valid_braces(s)) std::cout << "Expected " << s << " to be valid." << std::endl; \
  Assert::That(valid_braces(s), Equals(true));
#define assert_invalid(s) \
  if(valid_braces(s)) std::cout << "Expected " << s << " to be invalid." << std::endl; \
  Assert::That(valid_braces(s), Equals(false)); 

Describe(valid_braces_algorithm)
{
  It(basic_tests)
  {
    assert_valid( "()" );
    assert_invalid( "[(])" );
  }
};
*/


/*
Solutions from codewars

=1=
#include <regex>

bool valid_braces(std::string s) {
  std::regex r ("\\(\\)|\\[\\]|\\{\\}");
  while (std::regex_search(s, r)) s = std::regex_replace(s, r, "");
  return s.length() == 0;
}

=2=
bool valid_braces(std::string braces, std::stack<char> s = {}) 
{
  for(auto x : braces)
    if(!s.empty() && ((x=='}' && s.top() == '{') || (x==']' && s.top() == '[') || (x==')' && s.top() == '('))) s.pop();
    else s.push(x);
  return s.empty();
}
*/