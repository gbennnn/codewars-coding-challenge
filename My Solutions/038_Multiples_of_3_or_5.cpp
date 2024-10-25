/*
Codewars Coding Challenge

Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

Courtesy of projecteuler.net (Problem 1)


int solution(int number) 
{

}


https://www.codewars.com/kata/514b92a657cdc65150000006/train/cpp

*/



// My Solution
#include <iostream>
using namespace std;

int solution(int number) {
    int result = 0;
    if(number < 0){
        return 0;
    }
    cout << "Number = ";
    for( int i = 1; i < number; ++i){
        if(i % 3 == 0 || i % 5 == 0){
            cout << i << " ";
            result += i;
        }
    }
    cout << "\nResult = " << result << endl;
    return result;
}

// int main(){
//     cout << solution(10);

//     return 0;
// }



/*
Sample Tests

Describe(solution_algorithm)
{
    It(should_handle_basic_test_cases)
    {
        Assert::That(solution(10), Equals(23));
    }
};
*/