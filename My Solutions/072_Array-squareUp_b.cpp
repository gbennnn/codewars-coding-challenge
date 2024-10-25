/*
Codewars Coding Challenge

Day 72/366

Level 7kyu

Array - squareUp b!

This is a question from codingbat

Given an integer n greater than or equal to 0, create and return an array with the following pattern:

squareUp(3) => [0, 0, 1, 0, 2, 1, 3, 2, 1]
squareUp(2) => [0, 1, 2, 1]
squareUp(4) => [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]
0 <= n <= 1000.


using namespace std;

vector<int> squareUp(int n)
{
    return {};  // Do your magic!
}

https://www.codewars.com/kata/5a8bcd980025e99381000099/train/cpp

*/

// My Solution
#include <iostream>
#include <vector>
using namespace std;

vector<int> squareUp(int n){
    vector<int> result(n * n);

    for(int i = 1; i <= n; ++i){
        for(int j = 1; j <= i; ++j){
            result[n * i - j] = j;
        }
    }
    return result;
}

// Test
int main(){

    // Test 1
    vector<int> test1 = squareUp(3);
    for(int i : test1){
        cout << i << " ";
    }

    cout << endl;

    // Test 2
    vector<int> test2 = squareUp(2);
    for(int i : test2){
        cout << i << " ";
    }

    cout << endl;

    // Test 3
    vector<int> test3 = squareUp(4);
    for(int i : test3){
        cout << i << " ";
    }
    
    return 0;
}


/*
Sample Tests

using namespace std;

Describe(Tests)
{
    It(Basic_Tests)
    {
        doTest(4, {0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1});
        doTest(9, {0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 3, 2, 1, 0, 0, 0, 0, 0, 4, 3, 2, 1, 0, 0, 0, 0, 5, 4, 3, 2, 1, 0, 0, 0, 6, 5, 4, 3, 2, 1, 0, 0, 7, 6, 5, 4, 3, 2, 1, 0, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1});
        doTest(1, {1});
    }

    void doTest(int n, const vector<int> &expected)
    {
        Assert::That(vectorToString(squareUp(n)), Equals(vectorToString(expected)));
    }

    string vectorToString(const vector<int> &v)
    {
        stringstream ss;
        for (auto e : v) ss << to_string(e) << ", ";
        return '{' + ss.str().substr(0, ss.str().size()-2) + '}';
    }
};
*/
