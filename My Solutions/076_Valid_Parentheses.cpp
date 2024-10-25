/*
Codewars Coding Challenge 

Day 76/366

Level 7kyu

Valid Parentheses

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= length of input <= 100

All inputs will be strings, consisting only of characters ( and ).
Empty strings are considered balanced (and therefore valid), and will be tested.
For languages with mutable strings, the inputs should not be mutated.

Protip: If you are trying to figure out why a string of parentheses is invalid, paste the parentheses into the code editor, and let the code highlighting show you!


#include <string>

bool validParentheses(const std::string& str) {
    return false;
}

https://www.codewars.com/kata/6411b91a5e71b915d237332d/train/cpp

*/

// My Solutions
#include <string>
#include <stack>
#include <iostream>

bool validParentheses(const std::string& str) {
    std::stack<char> parenStack;

    for(char c : str){
        if(c == '('){
            parenStack.push(c);
        }else if (c == ')'){
            if (parenStack.empty()){
                return false; // kurung tutup tanpa pasangan
            }else{
                parenStack.pop(); // hapus kurung buka teratas
            }
        }
    }
    return parenStack.empty(); // return true jika semua kurung buka memiliki pasangan
}


// Test cases
int main(){
    std::cout << validParentheses("(") << std::endl;
    std::cout << validParentheses("(())((()())())") << std::endl;
    std::cout << validParentheses("()") << std::endl;
    std::cout << validParentheses(")(()))") << std::endl;
}




/*
Sample Tests

#include <string>

bool validParentheses(const std::string& str);
  
// TODO: Replace examples and use TDD by writing your own tests

Describe(SampleTests)
{
  It(ValidCases)
  {
    dotest("()",                 true);
    dotest("((()))",             true);
    dotest("()()()",             true);
    dotest("(()())()",           true);
    dotest("()(())((()))(())()", true);
  }

  It(EmptyString) {
    dotest("", true);
  }

  It(InvalidCases) {
    dotest(")(",     false);
    dotest("()()(",  false);
    dotest("((())",  false);
    dotest("())(()", false);
    dotest(")()",    false);
    dotest(")",      false);
  }
  
private:
  void dotest(const std::string& str, bool expected) { 
    bool actual = validParentheses(str);
    auto msg    = ExtraMessage("Incorrect answer for input = \"" + str + "\"");
    Assert::That(actual, Equals(expected), msg);
  }
};
*/


/*
Solutions from codewars

=1=
#include <string>

bool validParentheses(const std::string& str) {
    int open = 0;
    for(char c : str) {
        if((open += c == '(' ? 1 : -1) < 0) {
        return false;
        }
    }
    return !open;
}


=2=
#include <regex>
#include <string>

bool validParentheses(const std::string& str) {
    try {
        return std::regex{str}, true;
    } catch (std::regex_error) {
        return false;
    }
}


=3=
bool validParentheses( const std::string& str ) {
    std::stack< char > s;
    for ( const char c : str )
        if ( c == '(' ) s.push( c );
        else if ( !s.empty() && s.top() == '(' ) s.pop();
            else return false;
    return s.empty();
    }


=4=
    bool validParentheses(const std::string& str){
    int a = 0;
    for(char c : str)
        if((a += c == '(' ? 1 : -1) < 0)
        return 0;
        
    return !a;
    }
*/